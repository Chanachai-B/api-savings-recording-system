from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import transaction_routes
from app.core.config import Config

app = FastAPI(title="School Savings API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.API_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaction_routes.router, prefix="/transactions", tags=["Transactions"])

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")
