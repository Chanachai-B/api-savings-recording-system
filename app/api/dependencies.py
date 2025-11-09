from fastapi import Depends
from app.infrastructure.google_sheets.transaction_repository_impl import TransactionRepositoryImpl
from app.controllers.transaction_controller import TransactionController

def get_transaction_repository():
    return TransactionRepositoryImpl()

def get_transaction_controller(
    repo: TransactionRepositoryImpl = Depends(get_transaction_repository)
):
    return TransactionController(repo)
