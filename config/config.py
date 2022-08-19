from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class for defining all variables."""
    cf_handle: str = 'DmitriyH'
    base_dir: str = str(Path(__file__).parent.parent)
    acronym_ignore: list = ['and']

    class Config:
        """Config class."""
        env_file = str(Path(__file__).parent.parent) + '/config/.env'


settings = Settings()
