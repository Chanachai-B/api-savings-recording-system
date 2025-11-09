from app.domain.entities.transaction import Transaction
from app.domain.interfaces.transaction_repository import TransactionRepository
from app.schemas.transaction_schema import TransactionRequest, TransactionResponse, TransactionRequest
from typing import List

class TransactionController:
    def __init__(self, repo: TransactionRepository):
        self.repo = repo
        
    def list_transactions(self) -> List[TransactionResponse]:
        records = self.repo.get_all()
        return [TransactionResponse(**r) for r in records]

    def deposit(self, req: TransactionRequest) -> TransactionResponse:
        transaction = Transaction(req.student_id, req.student_name, req.date, req.amount, "deposit", req.note)

        if not transaction.is_valid():
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0 บาท")

        result = self.repo.add(transaction)
        return TransactionResponse(**result)
    
    def withdraw(self, req: TransactionRequest) -> TransactionResponse:
        transaction = Transaction(req.student_id, req.student_name, req.date, req.amount, "withdraw", req.note)

        if not transaction.is_valid():
            raise ValueError("จำนวนเงินถอนต้องมากกว่า 0 บาท")

        result = self.repo.add(transaction)
        return TransactionResponse(**result)
