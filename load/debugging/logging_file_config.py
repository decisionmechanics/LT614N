import logging
import logging.config

logging.config.fileConfig(fname="logging.ini")
logger = logging.getLogger("appLogger")

logger.debug("This is a debug message")
