import logging


def get_core_logger() -> logging.Logger:
    return logging.getLogger("core")


def get_custom_logger(logger_name: str) -> logging.Logger:
    return logging.getLogger(logger_name)
