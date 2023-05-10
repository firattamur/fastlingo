from enum import Enum


class TranslateService(Enum):
    """Enum for the different translation services."""

    GOOGLE = "google"
    MICROSOFT = "microsoft"
    YANDEX = "yandex"
    DEEPL = "deepl"
