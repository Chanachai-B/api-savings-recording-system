from typing import Literal
from fastapi import APIRouter, Depends

from app.api.dependencies import get_student_controller
from app.controllers.student_controller import StudentController
from app.schemas.student_schema import StudentResponse


router = APIRouter()

@router.get("/all", response_model=list[StudentResponse])
def list_student(
    controller: StudentController = Depends(get_student_controller)
):
    return controller.list_Students()

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: str, 
    controller: StudentController = Depends(get_student_controller)
):
    return controller.get_student(student_id)

@router.get("/{student_id}/index", response_model=int)
def get_row_student(
    student_id: str, 
    controller: StudentController = Depends(get_student_controller)
):
    return controller.get_row_data_student_in_db(student_id)

@router.put("/{student_id}/update_balance", response_model=StudentResponse)
def update_balance(
    student_id: str,
    amount: int,
    transaction_type: Literal["deposit", "withdraw"],
    controller: StudentController = Depends(get_student_controller)
):
    return controller.update_balance_student(student_id, amount, transaction_type)

