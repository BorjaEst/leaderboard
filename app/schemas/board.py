from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel

from app.typing import Order


# Shared properties
class BoardBase(BaseModel):
    pass


# Properties to receive on board creation
class BoardCreate(BoardBase):
    order: Order


# Properties to receive on board update
class BoardUpdate(BoardBase):
    pass


# Properties shared by models stored in DB
class BoardInDBBase(BoardBase):
    id: UUID
    order: Order


# Properties to return to client
class Board(BoardInDBBase):
    pass


# Properties properties stored in DB
class BoardInDB(BoardInDBBase):
    pass
