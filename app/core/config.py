import os
import json
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

class Config:
    API_ALLOW_ORIGINS = os.getenv("API_ALLOW_ORIGINS")
    SHEET_NAME = os.getenv("SHEET_NAME", "ชีตไม่ระบุชื่อ")
    SHEET_TAB_STUDENT = os.getenv("SHEET_TAB_STUDENT", "ชีต1")
    SHEET_TAB_TRANSACTION = os.getenv("SHEET_TAB_TRANSACTION", "ชีต2")
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    @classmethod
    def get_google_credentials(self):
        creds_dict = json.loads(os.getenv("GOOGLE_CREDENTIAL"))
        return Credentials.from_service_account_info(creds_dict, scopes=self.SCOPES)
