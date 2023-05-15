"""Module for configuring leaderboard generic fixtures"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
import pytest
from leaderboard import Leaderboard


@pytest.fixture(scope="session", param=["default", "config2"])
def config(request):
    return f".tests/test_configurations/{request.param}.toml"


@pytest.fixture(scope="session")
def leaderboard(config):
    yield Leaderboard('name', config_file=config)
