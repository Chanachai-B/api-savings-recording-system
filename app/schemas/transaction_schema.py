from pydantic import BaseModel, Field

class TransactionRequest(BaseModel):
    student_id: str = Field(..., example="ST001")
    student_name: str
    date: str
    amount: float | int | str = Field(..., gt=0, example=50.0)
    note: str

class TransactionResponse(BaseModel):
    transaction_id: str
    student_id: str
    student_name: str
    date: str
    deposit: str
    withdrawal: str
    balance: str
    note: str
    transaction_time_stamp: str
