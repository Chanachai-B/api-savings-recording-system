from typing import Any, Dict, List
import gspread
from app.core.config import Config
from app.core.utils import to_decimal_str
from app.domain.interfaces.student_repository import StudentRepository


class StudentRepositoryImpl(StudentRepository):
    """
    Repository implementation for managing student in Google Sheets.
    """

    def __init__(self):
        creds = Config.get_google_credentials()
        client = gspread.authorize(creds)
        self.sheet = client.open(Config.SHEET_NAME).worksheet(Config.SHEET_TAB_STUDENT)
        
    def get_all(self) -> List[Dict[str, Any]]:
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