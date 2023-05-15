"""Leaderboard module."""
from typing import Literal

from pydantic import BaseModel, validator, RedisDsn
from pydantic.types import PositiveInt

from app import config
from redis import StrictRedis, Redis, ConnectionPool


class Options(BaseModel):
    redis_host: RedisDsn = config.DEFAULT_REDIS_HOST
    redis_port: int = config.DEFAULT_REDIS_PORT
    redis_db: PositiveInt = config.DEFAULT_REDIS_DB
    order: Literal['ascendent', 'descendent'] = config.DEFAULT_POOL_ORDER

    @validator('redis_port')
    def valid_port(cls, port, values, **kwargs):
        if port < 0 or port > 65535:
            raise ValueError('Port value {port} is not a valid port.')
        return port


class Leaderboard(object):

    def __init__(self, leaderboard_name, **options):
        self.leaderboard_name = leaderboard_name
        self.config = Options(**options)
        self.redis_connection = Redis(**self.options)
