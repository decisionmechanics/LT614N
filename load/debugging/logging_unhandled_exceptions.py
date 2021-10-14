import logging
import logging.config
import sys

logging.config.fileConfig(fname="logging.ini")
logger = logging.getLogger("appLogger")


def handle_exception(exc_type, exc_value, exc_traceback):
    # Allow a console program to exit with ^C
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

        return

    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception

a = 1
b = 0

c = a / b
