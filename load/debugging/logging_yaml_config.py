import logging
import logging.config
import yaml

with open("logging.yml") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("appLogger")

logger.debug("This is a debug message")
