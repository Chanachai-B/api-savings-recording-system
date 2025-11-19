from abc import ABC, abstractmethod
from typing import Literal
from app.schemas.student_schema import StudentResponse

class StudentRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[dict]:
        pass
    
    @abstractmethod
    def get_student(student_id: str, records: list[StudentResponse]) -> StudentResponse | None:
        pass
    
    @abstractmethod
    def get_row_data_student_in_db(student_id: str, records: list[StudentResponse]) -> int | None:
        pass
    
    @abstractmethod
    def edit_student_data(self):
        pass
    
    @abstractmethod
    def calculate_balance(self, student_id: str, amount: int, transaction_type: Literal["deposit", "withdraw"], records: list[StudentResponse], idx: int):
        pass
    
