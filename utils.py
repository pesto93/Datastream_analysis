# _author_ = Johnleonard C.O
# _Date_ = 6/5/2020
import sys
import logging


def _configure_logger() -> logging.Logger:
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - Data Stream - %(message)s"
    )
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger


# Global scope
log_set = _configure_logger()
