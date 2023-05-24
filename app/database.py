import redis

from app.config import settings


def redis_connection():
    return redis.from_url(settings.redis_dsn)


def redis_pipeline():
    return redis_connection().pipeline()
