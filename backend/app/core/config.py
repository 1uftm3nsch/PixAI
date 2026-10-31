from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "PixAI Backend"
    API_V1_STR: str = "/api/v1"
    USE_MOCK_AI: bool = True
    GEMINI_API_KEY: Optional[str] = None
    REPLICATE_API_TOKEN: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

