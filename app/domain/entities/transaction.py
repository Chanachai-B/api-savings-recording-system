from datetime import datetime
from typing import Literal

class Transaction:
    def __init__(
        self, student_id: str, student_name: str,
        date: str, amount: float, transaction_type: Literal["deposit", "withdraw"],  note: str
    ):
        self.student_id = student_id
        self.student_name = student_name
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type
        self.note = note
        self.transaction_time_stamp = datetime.now()

    def is_valid(self) -> bool:
        """ตรวจสอบความถูกต้องของธุรกรรม"""
        return self.amount > 0 and self.transaction_type in ["deposit", "withdraw"]
