from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=str, status_code=201)
def metadata() -> Any:
    """Retrieve leaderboard application metadata.
    """
    raise NotImplementedError


@router.post("/test-message/", response_model=str, status_code=201)
def test_message(
    message: str,
) -> Any:
    """Echoes a message from server.
    """
    return message
