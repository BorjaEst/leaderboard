from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException

from app.database import redis_pipeline

Items = dict[str, Union[float, int]]
router = APIRouter()


@router.get("/boards", response_model=List[str])
def read_boards(
    pipeline=Depends(redis_pipeline),
):
    """Retrieve boards.
    """
    try:
        pipeline.scan()
        return pipeline.execute()[0][1]
    except Exception:
        raise HTTPException(status_code=500)


@router.delete("/boards", status_code=204)
def delete_board(
    boards: List[str],
    pipeline=Depends(redis_pipeline),
):
    """Delete boards.
    """
    try:
        for leaderboard_name in boards:
            pipeline.delete(leaderboard_name)
        return pipeline.execute()
    except Exception:
        raise HTTPException(status_code=500)


@router.get("/top-members", response_model=Items)
def get_members(
    name: str, n: int,
    pipeline=Depends(redis_pipeline),
):
    """Retrieve pool items.
    """
    try:
        pipeline.zrevrange(name, 0, n, withscores=True)
        return pipeline.execute()[0]
    except Exception:
        raise HTTPException(status_code=500)


@router.post("/rank-members", status_code=201)
def rank_members(
    boards: List[str], members: Items,
    pipeline=Depends(redis_pipeline),
):
    """Echoes a message from server.
    """
    try:
        for leaderboard_name in boards:
            pipeline.zadd(leaderboard_name, members)
        return pipeline.execute()
    except Exception:
        raise HTTPException(status_code=500)
