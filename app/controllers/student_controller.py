from typing import List, Literal
from app.domain.interfaces.student_repository import StudentRepository
from app.schemas.student_schema import StudentResponse

class StudentController:
    def __init__(self, repo: StudentRepository):
        self.repo = repo
        
    def list_Students(self) -> List[StudentResponse]:
        records = self.repo.get_all()
        return [StudentResponse(**r) for r in records]
    
    def get_student(self, student_id: str):
        records = self.repo.get_all()
        student_data = self.repo.get_student(student_id, records)
        return student_data
    
    def get_row_data_student_in_db(self, student_id: str):
        records = self.repo.get_all()
        idx = self.repo.get_row_data_student_in_db(student_id, records)
        return idx
    
    def update_balance_student(self, student_id: str, amount: int, transaction_type: Literal["deposit", "withdraw"]):
        records = self.repo.get_all()
        idx = self.repo.get_row_data_student_in_db(student_id, records)
        result = self.repo.calculate_balance(student_id, amount, transaction_type, records, idx)
        return result
