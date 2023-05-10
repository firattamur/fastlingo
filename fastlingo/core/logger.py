import logging


class Logger:
    """Custom Logger class to log the output a file and console"""

    def __init__(self, name: str) -> None:
        """Initialize the logger object

        Args:
            name (str): Name of the logger
            file (str): Path to the log file
        """

        log_format = "[%(asctime)s] - [%(levelname)s] - %(message)s"
        logging.basicConfig(level=logging.INFO, format=log_format)

        self._logger = logging.getLogger(name)

    def get_logger(self) -> logging.Logger:
        """Returns the logger object

        Returns:
            logging.Logger: Logger object
        """

        return self._logger
