from functools import lru_cache
from pathlib import Path
from typing import Literal
import os

from dotenv import load_dotenv
from pydantic import BaseModel


# Project root (taskify-api/)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env if present
load_dotenv(BASE_DIR / ".env")


class Settings(BaseModel):
    app_name: str = "Taskify API"
    environment: Literal["local", "dev", "prod"] = "local"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./taskify.db")

    class Config:
        frozen = True  # make it immutable


@lru_cache
def get_settings() -> Settings:
    return Settings()