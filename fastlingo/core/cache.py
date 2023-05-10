import json
import os
from abc import ABC, abstractmethod
from typing import Optional

from fastlingo.core.double_linked_list import DoubleLinkedList, Node


class Cache(ABC):
    """Abstract class for cache implementations."""

    def __init__(self, max_size: int = 1000) -> None:
        """Initialize the cache."""

        self._cache: dict = {}
        self._max_size = max_size
        self._list: DoubleLinkedList = DoubleLinkedList()

    @abstractmethod
    def get(self, key: str) -> Optional[str]:
        """Get a value from the cache.

        Args:
            key (str): The key of the value to get.

        Returns:
            str: The value of the key.
        """
        pass

    @abstractmethod
    def set(self, key: str, value: str) -> None:
        """Set a value in the cache.

        Args:
            key   (str): The key of the value to set.
            value (str): The value to set.
        """
        pass

    def save_to_file(self, file_path: str) -> None:
        """Save the LRUCache object to a file.

        Args:
            file_path (str): The path to the file where the LRUCache object will be saved.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file)

    @classmethod
    def load_from_file(cls, file_path: str):
        """Load an LRUCache object from a file.

        Args:
            file_path (str): The path to the file from which the LRUCache object will be loaded.

        Returns:
            LRUCache: An LRUCache object loaded from the file.
        """

        if not os.path.exists(file_path):
            return cls()

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return cls.from_dict(data)

    def to_dict(self) -> dict:
        """Convert the LRUCache object to a dictionary.

        Returns:
            dict: A dictionary representation of the LRUCache object.
        """
        cache_dict = {}
        for key, value in self._cache.items():
            cache_dict[key] = value.to_dict()

        return cache_dict

    @classmethod
    def from_dict(cls, data: dict):
        """Create an LRUCache object from a dictionary.

        Args:
            data (dict): A dictionary containing the LRUCache object data.

        Returns:
            LRUCache: An LRUCache object created from the dictionary.
        """
        lru_cache = cls()
        for key, value_data in data.items():
            node = Node.from_dict(value_data)
            lru_cache._cache[key] = node
        return lru_cache
