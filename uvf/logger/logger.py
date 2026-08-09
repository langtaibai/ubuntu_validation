import logging
import os

def get_logger(name="uvf"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s " 
        "%(levelname)s " 
        "%(name)s : " 
        "%(message)s"
    )

    file_handler = logging.FileHandler(
        "logs/uvf.log"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger