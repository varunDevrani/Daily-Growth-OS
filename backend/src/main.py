from fastapi import FastAPI

from src.database.database import engine
from src.exceptions import register_exception_handlers
from src.models.base import Base
from src.routes.auth import router as auth_router

app = FastAPI()


Base.metadata.create_all(
	bind=engine
)


register_exception_handlers(app)

@app.get("/")
def health_check():
    return {
    	"status": "backend running"
    }

app.include_router(auth_router, prefix="/api/v1")
