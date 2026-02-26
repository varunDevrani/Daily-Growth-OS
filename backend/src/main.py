from fastapi import FastAPI
from src.database.base import Base
from src.database.database import engine
from src.routes.auth import router as auth_router
from src.exceptions import register_exception_handlers

app = FastAPI(title="Daily Growth OS")

Base.metadata.create_all(bind=engine)


register_exception_handlers(app)


app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"status": "Backend running"}