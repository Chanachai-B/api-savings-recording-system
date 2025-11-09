import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_CREDENTIAL = os.getenv("GOOGLE_CREDENTIAL", "service_account.json")
    SHEET_NAME = os.getenv("SHEET_NAME", "ชีตไม่ระบุชื่อ")
    SHEET_TAB = os.getenv("SHEET_TAB", "ชีต1")
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
