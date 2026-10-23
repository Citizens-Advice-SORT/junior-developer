from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Citizens Advice SORT Junior Developer API"
    model_id: str = "fastino/GLiNER2-Guardrails-PII-Multi"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
