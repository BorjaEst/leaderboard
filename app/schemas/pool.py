from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel

from app.typing import Order


# Shared properties
class PoolBase(BaseModel):
    pass


# Properties to receive on pool creation
class PoolCreate(PoolBase):
    order: Order


# Properties to receive on pool update
class PoolUpdate(PoolBase):
    pass


# Properties shared by models stored in DB
class PoolInDBBase(PoolBase):
    id: UUID
    order: Order


# Properties to return to client
class Pool(PoolInDBBase):
    pass


# Properties properties stored in DB
class PoolInDB(PoolInDBBase):
    pass
