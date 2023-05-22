from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app import schemas

router = APIRouter()


@router.get("/{id}", response_model=List[schemas.Item])
def read_items(id: UUID):
    """Retrieve pool items.
    """
    raise NotImplementedError


@router.put("/{id}", response_model=schemas.Item)
def define_item(
    id: UUID,
    item_in: schemas.ItemUpdate,
):
    """Update an item.
    """
    raise NotImplementedError


@router.delete("/{id}", response_model=schemas.Item)
def delete_item(
    id: UUID,
):
    """Delete an item.
    """
    raise NotImplementedError
