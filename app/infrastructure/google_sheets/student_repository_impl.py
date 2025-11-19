from typing import Literal
import gspread
from app.core.config import Config
from app.core.utils import to_decimal_str
from app.domain.interfaces.student_repository import StudentRepository
import polars as pl

from app.schemas.student_schema import Student, UpdateBalanceRequest

class StudentRepositoryImpl(StudentRepository):
    """
    Repository implementation for managing student in Google Sheets.
    """

    def __init__(self):
        creds = Config.get_google_credentials()
        client = gspread.authorize(creds)
        self.sheet = client.open(Config.SHEET_NAME).worksheet(Config.SHEET_TAB_STUDENT)
        
    def get_all(self) -> list[dict[str, any]]:
        """ดึงข้อมูลธุรกรรมทั้งหมดจาก Sheet"""
        records = self.sheet.get_all_records()
        cleaned_records = []

        for record in records:
            clean_row = {}
            for key, value in record.items():
                if key in ("number", "student_id"):
                    clean_row[key] = to_decimal_str(value, digits=0)
                else:
                    clean_row[key] = str(value)
            cleaned_records.append(clean_row)

        return cleaned_records
    
    def get_student(self, student_id: str, records: list[dict[str, any]]):
        df_records = pl.DataFrame(records)
        df_student_data = df_records.filter(pl.col("student_id") == student_id)
        student_result = df_student_data.to_dicts()
        return student_result[0] if student_result.__len__() > 0 else None
    
    def get_row_data_student_in_db(self, student_id: str, records: list[UpdateBalanceRequest]):
        df_records = pl.DataFrame(records)
        try:
            idx = df_records.select(
                pl.arg_where(pl.col("student_id") == student_id)
            ).item()
        except:
            idx = None
        return idx
    
    def edit_student_data(self,records, academic_year, classroom, number, student_id, prefix, first_name, last_name, total_deposit, total_withdrawal, balance):
        # records = self.sheet.get_all_records()
        pass
        
    def calculate_balance(self, student_id: str, amount: int, transaction_type: Literal["deposit", "withdraw"], records: list[UpdateBalanceRequest], idx: int):
        df_records = pl.DataFrame(records)
        df_student_data = df_records.filter(pl.col("student_id") == student_id)
        student_data = df_student_data.to_dicts()[0] if df_student_data.to_dicts().__len__() > 0 else None
        
        sheet_row = idx + 2
        keys = Student.model_fields.keys()
        keys_list = list(keys)
        col_balance = keys_list.index("balance") + 1
        col_total_deposit = keys_list.index("total_deposit") + 1 if transaction_type == "deposit" else None
        col_total_withdrawal = keys_list.index("total_withdrawal") + 1 if transaction_type == "withdraw" else None

        if student_data and transaction_type == "deposit":
            last_deposit = float(student_data.get("total_deposit", 0.00))
            balance = float(student_data.get("balance", 0.00))
            total_balance = balance + amount
            total_deposit = last_deposit + amount
            student_data["balance"] = to_decimal_str(total_balance)
            student_data["total_deposit"] = to_decimal_str(total_deposit)
            self.sheet.update_cell(sheet_row, col_total_deposit, student_data["total_deposit"])
        elif student_data and transaction_type == "withdraw":
            last_withdrawal = float(student_data.get("total_withdrawal", 0.00))
            balance = float(student_data.get("balance", 0.00))
            total_balance = balance - amount
            total_withdrawal = last_withdrawal + amount
            student_data["balance"] = to_decimal_str(total_balance)
            student_data["total_withdrawal"] = to_decimal_str(total_withdrawal)
            self.sheet.update_cell(sheet_row, col_total_withdrawal, student_data["total_withdrawal"])
        else:
            return None
        self.sheet.update_cell(sheet_row, col_balance, student_data["balance"])
        return student_data

        