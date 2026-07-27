"""
Application Logger
"""

import logging

import sys


LOGGER_NAME = "crisisops"


logger = logging.getLogger(

    LOGGER_NAME

)


if not logger.handlers:

    handler = logging.StreamHandler(

        sys.stdout

    )

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )

    handler.setFormatter(

        formatter

    )

    logger.addHandler(

        handler

    )

    logger.setLevel(

        logging.INFO

    )


def get_logger(

    name: str = LOGGER_NAME,

):

    return logging.getLogger(name)