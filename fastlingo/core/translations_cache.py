import os
from typing import Optional

from fastlingo.core.cache_lru import CacheLRU
from fastlingo.core.utils import create_hash_key


class TranslationsCache:
    """Cache for translations."""

    def __init__(self, folder: str = ".fastlingo-cache") -> None:
        """Initialize the cache.

        Args:
            max_size (int, optional): The maximum size of the cache. Defaults to 1000.
            folder   (str, optional): The folder to store the cache in. Defaults to ".fastlingo-cache".
        """

        self._cache: CacheLRU = CacheLRU()
        self._folder: str = folder

        if not os.path.exists(self._folder):
            os.makedirs(self._folder)

    def get(
        self, source_language: str, target_language: str, text: str
    ) -> Optional[str]:
        """Get a translation from the cache.

        Args:
            source_language (str): The source language.
            target_language (str): The target language.
            text            (str): The text.

        Returns:
            str: The translation.
        """
        self._load_cache(source_language, target_language)
        key = create_hash_key(source_language, target_language, text)

        return self._cache.get(key)

    def set(
        self, source_language: str, target_language: str, text: str, translation: str
    ) -> None:
        """Set a translation in the cache.

        Args:
            source_language (str): The source language.
            target_language (str): The target language.
            text            (str): The text.
            translation     (str): The translation.
        """
        self._load_cache(source_language, target_language)

        key = create_hash_key(source_language, target_language, text)
        self._cache.set(key, translation)

        self._save_cache(source_language, target_language)

    def _get_cache_file_path(self, source_language: str, target_language: str) -> str:
        """Get the path to the cache file.

        Args:
            source_language (str): The source language.
            target_language (str): The target language.

        Returns:
            str: The path to the cache file.
        """

        return f"{self._folder}/{source_language}-{target_language}.json"

    def _load_cache(self, source_language: str, target_language: str) -> None:
        """Load the cache from a file.

        Args:
            source_language (str): The source language.
            target_language (str): The target language.
        """

        cache_file_path = self._get_cache_file_path(source_language, target_language)
        self._cache = CacheLRU.load_from_file(cache_file_path)

    def _save_cache(self, source_language: str, target_language: str) -> None:
        """Save the cache to a file.

        Args:
            source_language (str): The source language.
            target_language (str): The target language.
        """

        cache_file_path = self._get_cache_file_path(source_language, target_language)
        self._cache.save_to_file(cache_file_path)
