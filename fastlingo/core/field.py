from enum import Enum

from fastlingo.core.exceptions import FastLingoException


class Field(Enum):
    """Enum for the fields to translate."""

    NAME = "name"
    DESCRIPTION = "description"
    KEYWORDS = "keywords"
    RELEASE_NOTES = "release_notes"
    SUBTITLE = "subtitle"
    PROMOTIONAL_TEXT = "promotional_text"

    @classmethod
    def get_by_name(cls, name: str) -> "Field":
        """Get the field by the name.

        Args:
            name (str): The name.

        Returns:
            Field: The field.
        """
        try:
            return cls[name.upper()]
        except KeyError:
            raise FastLingoException(f"Field with name '{name}' not found.")

    @classmethod
    def get_fields_to_translate(cls, config_fields: list) -> list:
        """Get the fields to translate from the config file.

        Args:
            config_fields (list): The fields from the config file.

        Returns:
            list: The fields to translate.
        """
        if not config_fields:
            return list(cls)

        fields = [cls.get_by_name(field) for field in config_fields]
        return fields
