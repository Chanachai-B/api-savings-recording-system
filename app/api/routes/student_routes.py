from typing import List
from fastapi import APIRouter, Depends

from app.api.dependencies import get_student_controller
from app.controllers.student_controller import StudentController
from app.schemas.student_schema import StudentResponse


router = APIRouter()

@router.get("/all", response_model=List[StudentResponse])
def list_student(
    controller: StudentController = Depends(get_student_controller)
):
    return controller.list_Students()