from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"   # name of current enviroment
    base_url: str = "http://localhost:8000"    # domain of your host
    db_url: str = "sqlite:///./shortener.db"   # address of databse

    class Config:
        env_file = ".env"
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
