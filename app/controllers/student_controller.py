from typing import List
from app.domain.interfaces.student_repository import StudentRepository
from app.schemas.student_schema import StudentResponse


class StudentController:
    def __init__(self, repo: StudentRepository):
        self.repo = repo
        
    def list_Students(self) -> List[StudentResponse]:
        records = self.repo.get_all()
        print(records)
        return [StudentResponse(**r) for r in records]
