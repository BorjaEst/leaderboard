from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException

from app import schemas
from app.config import settings
from app.typing import Order
from app.leaderboard import Leaderboard


router = APIRouter()
boards = {}


@router.get("/", response_model=List[schemas.Board])
def read_boards():
    """Retrieve boards.
    """
    return [board.__dict__ for board in boards.values()]


@router.post("/", response_model=schemas.Board)
def create_board(order: Order = settings.default.order):
    """Create new board.
    """
    id = uuid4()
    boards[id] = Leaderboard(id, order=order)
    return boards[id].__dict__


@router.get("/{id}", response_model=schemas.Board)
def read_board(id: UUID):
    """Get board by ID.
    """
    try:
        return boards[id]
    except KeyError:
        raise HTTPException(status_code=404)


@router.delete("/{id}", response_model=None)
def delete_board(id: UUID):
    """Delete an board.
    """
    try:
        del boards[id]
    except KeyError:
        raise HTTPException(status_code=404)
