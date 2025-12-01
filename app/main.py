from fastapi import FastAPI

from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Task management API built with FastAPI and SQLAlchemy",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Taskify API is running",
        "environment": settings.environment,
        "database_url": settings.database_url,
    }