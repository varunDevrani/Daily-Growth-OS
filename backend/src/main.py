from fastapi import FastAPI
from src.database.base import Base
from src.database.database import engine

app = FastAPI(title="Daily Growth OS")

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "Backend running"}