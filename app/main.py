from fastapi import FastAPI
from app.api.routes import transaction_routes

app = FastAPI(title="School Savings API", version="1.0")

app.include_router(transaction_routes.router, prefix="/transactions", tags=["Transactions"])

@app.get("/")
def root():
    return {"message": "School Savings API is running 🚀"}
