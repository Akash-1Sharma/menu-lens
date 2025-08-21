from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = Field(default="Menu Lens API")
    ALLOWED_ORIGINS: str = Field(default="*")
    model_config = {
    "env_file": ".env",
    "env_file_encoding": "utf-8",
}
settings = Settings()

