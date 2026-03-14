import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Interviewer Platform"
    API_V1_STR: str = "/api/v1"
    
    # DATABASE
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db" 
    # For production: "postgresql+asyncpg://user:password@host:port/dbname"

    # SECURITY
    SECRET_KEY: str = "YOUR_SUPER_SECRET_KEY_CHANGE_IN_PRODUCTION"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # AI PROVIDERS
    GEMINI_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
