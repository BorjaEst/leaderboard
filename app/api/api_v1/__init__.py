from fastapi import APIRouter

from app.api.api_v1 import items, board, utils

router = APIRouter()
router.include_router(board.router, prefix="/board", tags=["board"])
router.include_router(items.router, prefix="/items", tags=["items"])
router.include_router(utils.router, tags=["utils"])
