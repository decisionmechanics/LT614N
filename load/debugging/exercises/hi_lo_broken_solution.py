import logging
import logging.config
import random
import sys


logger = None


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

        return

    logger.critical("uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def configure_logging():
    global logger

    logging.config.fileConfig(fname="hi_lo_logging.ini")
    logger = logging.getLogger("appLogger")

    sys.excepthook = handle_exception


def main():
    configure_logging()

    secret = random.randint(1, 100)
    # Don't log secrets such as passwords and API keys
    logger.debug(f"secret is {secret}")

    guess = 0
    attempts = 0

    while guess != secret:
        guess = input("What number am I thinking of? ")
        logger.debug(f"user guessed {guess}")

        tries += 1

        logger.debug(f"{attempts} attempt(s)")

        if guess <= secret:
            print(f"It's bigger than {guess}. Try again.")
        elif guess > secret:
            print(f"It's smaller than {guess}. Try again.")

    print(
        "Congratulations. You correctly guessed I was thinking of {secret} in {attempts} attempt(s)."
    )


if __name__ == "__main__":
    main()
