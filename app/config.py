from pydantic import BaseModel, BaseSettings, RedisDsn

from app.typing import Order


class Application(BaseModel):
    openapi_url: str = '/api/v1/openapi.json'


class Defaults(BaseModel):
    pool_order: Order = 'ascendant'


class Settings(BaseSettings):
    redis_om_url: RedisDsn = 'redis://@localhost:6379/1'
    v1_str: str = '/api/v1'
    app: Application = Application()
    default: Defaults = Defaults()

    class Config:
        env_nested_delimiter = '__'


settings = Settings()
defaults = settings.default
