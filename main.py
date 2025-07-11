from src.datascience import LoggerConfig

logger = LoggerConfig.get_logger()

logger.info("Service started")
logger.error("Something went wrong", exc_info=True)
