from pydantic import BaseModel, BaseSettings, AnyUrl, PositiveInt

from app.typing import Order


class Application(BaseModel):
    openapi_url: str = '/api/v1/openapi.json'


class Defaults(BaseModel):
    redis_host: AnyUrl = 'localhost'
    redis_port: PositiveInt = 6379
    redis_db: PositiveInt = 0
    page_size: PositiveInt = 25
    order: Order = 'ascendant'
    pools: dict = {}


class Settings(BaseSettings):
    v1_str: str = '/api/v1'
    app: Application = Application()
    default: Defaults = Defaults()

    class Config:
        env_nested_delimiter = '__'


settings = Settings()
defaults = settings.default
