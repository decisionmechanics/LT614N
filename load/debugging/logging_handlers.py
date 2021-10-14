import logging


def main():
    # Create a custom logger
    logger = logging.getLogger("appLogger")

    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("app.log")

    # Set reporting levels
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.ERROR)

    # Create formatters
    console_formatter = logging.Formatter("%(name)s %(levelname)s: %(message)s")
    file_formatter = logging.Formatter(
        "%(asctime)s %(name)s %(levelname)s [%(process)d]: %(message)s"
    )

    # Add formatters to handlers
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Log messages
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()