from fastapi import APIRouter

from app.api.api_v1 import items, pool, utils

router = APIRouter()
router.include_router(pool.router, prefix="/pools", tags=["pools"])
router.include_router(items.router, prefix="/items", tags=["items"])
router.include_router(utils.router, tags=["utils"])
