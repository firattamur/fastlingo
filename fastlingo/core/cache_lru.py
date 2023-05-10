from typing import Optional

from fastlingo.core.cache import Cache


class CacheLRU(Cache):
    """Cache implementation using a Least Recently Used (LRU) algorithm."""

    def __init__(self, max_size: int = 1000) -> None:
        """Initialize the cache."""
        super().__init__(max_size)

    def get(self, key: str) -> Optional[str]:
        """Get a value from the cache.

        Args:
            key (str): The key of the value to get.

        Returns:
            str: The value of the key.
        """
        if key in self._cache:
            self._list.move_to_end(self._cache[key])
            return self._cache[key].value
        else:
            return None

    def set(self, key: str, value: str) -> None:
        """Set a value in the cache.

        Args:
            key   (str): The key of the value to set.
            value (str): The value to set.
        """
        if key in self._cache:
            self._list.move_to_end(self._cache[key])
            self._cache[key].value = value

        else:
            self._list.append(key, value)
            self._cache[key] = self._list.tail

            if len(self._cache) > self._max_size:
                least_recently_used = self._list.head
                del self._cache[least_recently_used.key]

                self._list.remove(self._list.head)
