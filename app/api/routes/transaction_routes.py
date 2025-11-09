from fastapi import APIRouter, Depends
from app.api.dependencies import get_transaction_controller
from app.controllers.transaction_controller import TransactionController
from app.schemas.transaction_schema import TransactionRequest, TransactionResponse, TransactionRequest
from typing import List

router = APIRouter()

@router.get("/", response_model=List[TransactionResponse])
def list_transactions(
    controller: TransactionController = Depends(get_transaction_controller)
):
    return controller.list_transactions()

@router.post("/deposit", response_model=TransactionResponse)
def deposit(
    req: TransactionRequest,
    controller: TransactionController = Depends(get_transaction_controller)
):
    return controller.deposit(req)

@router.post("/withdraw", response_model=TransactionResponse)
def withdraw(
    req: TransactionRequest,
    controller: TransactionController = Depends(get_transaction_controller)
):
    return controller.withdraw(req)