from abc import ABCMeta, abstractmethod

from app.utils.file_utils import Config


class IGenerator(metaclass=ABCMeta):
    """Interface for creating svg handler class."""

    @classmethod
    @abstractmethod
    def generate(cls, config: Config):
        """An abstract interface method"""
