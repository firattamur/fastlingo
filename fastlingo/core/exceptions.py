class FastLingoException(Exception):
    """Base exception for all FastLingo exceptions."""

    def __init__(self, message: str) -> None:
        """Initialize a FastLingo exception.

        Args:
            message (str): The message.

        Returns:
            None
        """

        if message is None:
            message = "An error occurred in FastLingo."

        message = f"FastLingoException: {message}"

        super().__init__(message)
