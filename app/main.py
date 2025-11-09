from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import transaction_routes

app = FastAPI(title="School Savings API", version="1.0")

app.include_router(transaction_routes.router, prefix="/transactions", tags=["Transactions"])

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")
