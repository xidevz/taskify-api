from fastapi import FastAPI

app = FastAPI(
    title="Taskify API",
    version="0.1.0",
    description="Task management API built with FastAPI and PostgreSQL"
)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Taskify API is running"}
