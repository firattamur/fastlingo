import os

from fastlingo.core.exceptions import FastLingoException


class FileIO:
    """File IO helper class."""

    @staticmethod
    def read(file_path: str) -> str:
        """Read a txt file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The content of the file.
        """

        if not os.path.exists(file_path):
            raise FastLingoException(f"File '{file_path}' not found.")

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write(file_path: str, content: str) -> None:
        """Write a txt file.

        Args:
            file_path (str): The path to the file.
            content   (str): The content of the file.

        Returns:
            None
        """

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def get_field_file_path(metadata_folder: str, language: str, field: str) -> str:
        """Get the path to the field file.

        Args:
            metadata_folder (str): The path to the metadata folder.
            language        (str): The language.
            field           (str): The field.

        Returns:
            str: The path to the field file.
        """

        return f"{metadata_folder}/{language}/{field}.txt"
