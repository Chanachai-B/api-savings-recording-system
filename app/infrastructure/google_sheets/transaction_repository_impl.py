import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any
from app.domain.entities.transaction import Transaction
from app.domain.interfaces.transaction_repository import TransactionRepository
from app.core.config import Config
from app.core.utils import to_decimal_str

class TransactionRepositoryImpl(TransactionRepository):
    """
    Repository implementation for managing transactions in Google Sheets.
    Handles CRUD operations for deposit/withdrawal records.
    """

    def __init__(self):
        creds = Config.get_google_credentials()
        client = gspread.authorize(creds)
        self.sheet = client.open(Config.SHEET_NAME).worksheet(Config.SHEET_TAB_TRANSACTION)

    # ---------------------------------------------------------
    # Internal Helpers
    # ---------------------------------------------------------

    def _generate_transaction_id(self) -> str:
        """สร้างรหัสธุรกรรมอัตโนมัติ"""
        all_rows = self.sheet.get_all_values()
        next_id = len(all_rows)
        return str(next_id)

    def _get_last_transaction_for_student(self, student_id: str) -> Dict[str, Any]:
        """ดึงธุรกรรมล่าสุดของนักเรียน"""
        records = self.sheet.get_all_records()
        student_records = [r for r in records if str(r.get("student_id")) == student_id]
        return student_records[-1] if student_records else {}

    def _create_base_transaction(self, transaction: Transaction) -> Dict[str, Any]:
        """สร้าง template ธุรกรรมพื้นฐาน"""
        return {
            "transaction_id": self._generate_transaction_id(),
            "student_id": transaction.student_id,
            "student_name": transaction.student_name,
            "date": transaction.date,
            "deposit": "",
            "withdrawal": "",
            "balance": "",
            "note": transaction.note,
            "transaction_time_stamp": transaction.transaction_time_stamp.strftime("%Y-%m-%d %H:%M:%S"),
        }

    # ---------------------------------------------------------
    # Deposit / Withdraw Logic
    # ---------------------------------------------------------

    def _deposit(self, last_record: Dict[str, Any], transaction: Transaction) -> List[Any]:
        new_tx = self._create_base_transaction(transaction)
        deposit_amount = float(transaction.amount)
        last_balance = float(last_record.get("balance", 0) or 0.0)
        new_balance = last_balance + deposit_amount

        new_tx["deposit"] = to_decimal_str(deposit_amount)
        new_tx["balance"] = to_decimal_str(new_balance)
        return list(new_tx.values())

    def _withdraw(self, last_record: Dict[str, Any], transaction: Transaction) -> List[Any]:
        new_tx = self._create_base_transaction(transaction)
        withdraw_amount = float(transaction.amount)
        last_balance = float(last_record.get("balance", 0) or 0.0)
        
        if withdraw_amount > last_balance:
            raise ValueError("ยอดคงเหลือไม่เพียงพอสำหรับการถอน")

        new_balance = last_balance - withdraw_amount

        new_tx["withdrawal"] = to_decimal_str(withdraw_amount)
        new_tx["balance"] = to_decimal_str(new_balance)
        return list(new_tx.values())

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def add(self, transaction: Transaction) -> Dict[str, Any]:
        """เพิ่มข้อมูลธุรกรรมลงใน Google Sheet"""
        last_record = self._get_last_transaction_for_student(str(transaction.student_id))

        match transaction.transaction_type:
            case "deposit":
                row_values = self._deposit(last_record, transaction)
            case "withdraw":
                row_values = self._withdraw(last_record, transaction)
            case _:
                raise ValueError(f"Unknown transaction type: {transaction.transaction_type}")

        self.sheet.append_row(row_values)

        headers = [h.strip().lower() for h in self.sheet.row_values(1)]
        last_row = self.sheet.get_all_values()[-1]
        record_dict = dict(zip(headers, last_row))

        # normalize header typo
        if "withdraw" in record_dict and "withdrawal" not in record_dict:
            record_dict["withdrawal"] = record_dict.pop("withdraw")

        return record_dict

    def get_all(self) -> List[Dict[str, Any]]:
        """ดึงข้อมูลธุรกรรมทั้งหมดจาก Sheet"""
        records = self.sheet.get_all_records()
        cleaned_records = []

        for record in records:
            clean_row = {}
            for key, value in record.items():
                if key in ("deposit", "withdrawal", "balance"):
                    clean_row[key] = to_decimal_str(value)
                else:
                    clean_row[key] = str(value)
            cleaned_records.append(clean_row)

        return cleaned_records
