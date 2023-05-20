from redis_om import Field, HashModel
from uuid import UUID, uuid4

from app.config import defaults


class Pool(HashModel):
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    order: str = Field(index=True, default=defaults.pool_order)
