import logging
import logging.handlers as handlers
import sys
import time


def main():
    logger = logging.getLogger("timed_app")
    logger.setLevel(logging.DEBUG)

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setLevel(logging.DEBUG)
    logger.addHandler(consoleHandler)

    fileHandler = handlers.TimedRotatingFileHandler(
        "timed_app.log", when="M", interval=1
    )
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)

    count = 0

    while True:
        time.sleep(1)
        count += 1
        logger.debug(f"This is a debug message ({count})")


if __name__ == "__main__":
    main()
