from uuid import UUID, uuid4

from redis_om import Field, HashModel


class Item(HashModel):
    score: float = Field(index=True, default=0.0)
    id: UUID = Field(index=True, default_factory=uuid4)
    data: str = Field(default="")
