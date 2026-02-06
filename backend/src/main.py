from fastapi import FastAPI
from schemas.auth import SignupRequest , LoginRequest


app = FastAPI(title="Daily Growth OS")




@app.get("/")
def health_check():
    return {"status": "Backend running"}


