from pydantic import BaseModel, Field

class StudentRequest(BaseModel):
    # student_id: str = Field(..., example="ST001")
    # student_name: str
    # date: str
    # amount: float | int | str = Field(..., gt=0, example=50.0)
    # note: str
    pass

class Student(BaseModel):
    academic_year: str
    classroom: str
    number: str
    student_id: str
    prefix: str
    first_name: str
    last_name: str
    total_deposit: str
    total_withdrawal: str
    balance: str
class StudentResponse(Student):
    pass

class UpdateBalanceRequest(BaseModel):
    student_id: str
    total_deposit: str
    total_withdrawal: str
    balance: str
    
class UpdateBalanceResponse(UpdateBalanceRequest):
    pass