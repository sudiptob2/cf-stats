from abc import ABCMeta, abstractmethod


class IGenerator(metaclass=ABCMeta):
    """Interface for creating svg handler class."""

    @classmethod
    @abstractmethod
    def generate(cls):
        """An abstract interface method"""
