import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class for defining all variables."""
    cf_handle: str = 'sudipto.me'
    base_dir: str = str(Path(__file__).parent.parent)

    class Config:
        """Config class."""
        env_file = os.path.expanduser('config/.env')


settings = Settings()
