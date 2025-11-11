from fastapi import Depends
from app.controllers.student_controller import StudentController
from app.infrastructure.google_sheets.student_repository_impl import StudentRepositoryImpl
from app.infrastructure.google_sheets.transaction_repository_impl import TransactionRepositoryImpl
from app.controllers.transaction_controller import TransactionController

def get_student_repository():
    return StudentRepositoryImpl()

def get_student_controller(
    repo: StudentRepositoryImpl = Depends(get_student_repository)
):
    return StudentController(repo)

def get_transaction_repository():
    return TransactionRepositoryImpl()

def get_transaction_controller(
    repo: TransactionRepositoryImpl = Depends(get_transaction_repository)
):
    return TransactionController(repo)
