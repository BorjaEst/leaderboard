from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from app import models, schemas
from app.config import settings
from app.typing import Order

from redis_om import NotFoundError

router = APIRouter()


@router.get("/", response_model=List[UUID])
def read_pools():
    """Retrieve pools.
    """
    return models.Pool.all_pks()


@router.post("/", response_model=schemas.Pool)
def create_pool(order: Order = settings.default.pool_order):
    """Create new pool.
    """
    pool = models.Pool(order=order)
    pool.save()
    return pool.dict()


@router.get("/{id}", response_model=schemas.Pool)
def read_pool(id: UUID):
    """Get pool by ID.
    """
    try:
        return models.Pool.get(id)
    except NotFoundError:
        raise HTTPException(status_code=404)


@router.delete("/{id}", response_model=None)
def delete_pool(id: UUID):
    """Delete an pool.
    """
    models.Pool.delete(id)
