from pydantic import BaseModel, BaseSettings, RedisDsn


class Application(BaseModel):
    openapi_url: str = '/api/v1/openapi.json'


class Settings(BaseSettings):
    redis_dsn: RedisDsn = 'redis://@localhost:6379/1'
    v1_str: str = '/api/v1'
    app: Application = Application()

    class Config:
        env_nested_delimiter = '__'


settings = Settings()
