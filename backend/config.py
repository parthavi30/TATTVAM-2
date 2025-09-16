import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Application settings
    app_name: str = "Tattvam API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Security settings
    secret_key: str = "tattvam-secret-key-2024"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440  # 24 hours
    
    # Database settings (for future use)
    database_url: Optional[str] = None
    
    # CORS settings
    allowed_origins: list = [
        "http://localhost:3000",
        "http://frontend:3000",
        "http://localhost:80",
        "http://frontend:80"
    ]
    
    # API settings
    api_v1_prefix: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()