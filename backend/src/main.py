from fastapi import FastAPI
from src.routes.auth import router as auth_router

app = FastAPI(title="Daily Growth OS")



@app.get("/")
def health_check():
    return {"status": "Backend running"}

app.include_router(auth_router, prefix="/api/v1")
