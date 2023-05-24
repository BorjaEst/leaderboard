"""Module for configuring leaderboard generic fixtures"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
import pytest


@pytest.fixture(scope="session", param=["default", "config2"])
def config(request):
    return f".tests/test_configurations/{request.param}.toml"
