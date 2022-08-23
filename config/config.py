from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class for defining all variables."""
    cf_handle: str = 'DmitriyH'
    base_dir: str = str(Path(__file__).parent.parent)
    acronym_ignore: list = ['and']
    max_name_len: int = 13  # defines the max len of a cf user's full name, default 13

    class Config:
        """Config class."""
        env_file = str(Path(__file__).parent.parent) + '/config/.env'


settings = Settings()
