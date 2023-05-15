import pytest
from redis import ConnectionPool, Redis, StrictRedis


@pytest.mark.parametrize("config", ["default"])
def test_default_values(leaderboard):
    assert leaderboard.somethinng == True
