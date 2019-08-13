import logging
import os
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = os.path.abspath("") + "\\logs\\log.log"


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.info("Logger is set up")
    return logger


LOGGER = get_logger("test")
