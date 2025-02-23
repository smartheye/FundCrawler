from __future__ import annotations

from utils import getLogger # isort:skip
log = getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from dotenv import dotenv_values, load_dotenv
from dataclasses import dataclass
import os

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------
_config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.shared"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

__all__ = [
    "EnvConfig"
]
#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------
@dataclass
class EnvConfig:
    arangodb_url:str

    def __init__(self):
        self.arangodb_url = _config['ARANGODB_URL']
        self.timescaledb_url = _config['TIMESCALEDB_URL']
#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------