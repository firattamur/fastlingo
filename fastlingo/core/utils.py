import hashlib


def create_hash_key(source_language: str, target_language: str, text: str) -> str:
    """Create a hash from the source language, target language and text.

    Args:
        source_language (str): The source language.
        target_language (str): The target language.
        text            (str): The text.

    Returns:
        str: The hash.
    """

    return hashlib.sha256(
        f"{source_language}{target_language}{text}".encode("utf-8")
    ).hexdigest()
