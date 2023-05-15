import configparser
import os
import pathlib


# Get configuration from user env and merge with pkg settings
DEFAULTS_FILE = pathlib.Path(__file__).parent / "settings.ini"
SETTINGS_FILE = os.getenv("LEADERBOARD_SETTINGS", default="")
settings = configparser.ConfigParser()
settings.read(DEFAULTS_FILE)
settings.read(SETTINGS_FILE)


# -- Redis service configuration
try:  # Defines the default redis host to use on leaderboard init
    value = os.getenv("DEFAULT_REDIS_HOST", settings['redis']['host'])
    DEFAULT_REDIS_HOST = value
except KeyError as err:
    raise RuntimeError(f"Invalid redis host {err}") from err

try:  # Defines the default redis port to use on leaderboard init
    value = os.getenv("DEFAULT_REDIS_PORT", settings['redis']['port'])
    DEFAULT_REDIS_PORT = value
except KeyError as err:
    raise RuntimeError(f"Invalid redis port {err}") from err

try:  # Defines the default redis port to use on leaderboard init
    value = os.getenv("DEFAULT_REDIS_DB", settings['redis']['db'])
    DEFAULT_REDIS_DB = value
except KeyError as err:
    raise RuntimeError(f"Invalid redis database {err}") from err


# -- Leaderboard pool configuration
try:  # Defines the default pool order to use on leaderboard init
    value = os.getenv("DEFAULT_POOL_ORDER", settings['pool']['order'])
    DEFAULT_POOL_ORDER = value
except KeyError as err:
    raise RuntimeError(f"Invalid redis database {err}") from err
