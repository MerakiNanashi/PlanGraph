from core.utils.base import logging

# Function for logging setup
def get_logger(
    name: str,
) -> logging.Logger:

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    logger.propagate = False

    return logger