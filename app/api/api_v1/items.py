from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from app import models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def read_items(
    # db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """Retrieve items.
    """
    raise NotImplementedError


@router.post("/", response_model=schemas.Item)
def create_item(
    # db: Session = Depends(deps.get_db),
    item_in: schemas.ItemCreate,
) -> Any:
    """Create new item.
    """
    raise NotImplementedError


@router.put("/{id}", response_model=schemas.Item)
def update_item(
    # db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.ItemUpdate,
) -> Any:
    """Update an item.
    """
    raise NotImplementedError


@router.get("/{id}", response_model=schemas.Item)
def read_item(
    # db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """Get item by ID.
    """
    raise NotImplementedError


@router.delete("/{id}", response_model=schemas.Item)
def delete_item(
    # db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """Delete an item.
    """
    raise NotImplementedError
