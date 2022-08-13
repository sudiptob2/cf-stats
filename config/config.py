import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class for defining all variables."""
    cf_handle: str = 'sudipto.me'

    class Config:
        """Config class."""
        env_file = os.path.expanduser('config/.env')


settings = Settings()
