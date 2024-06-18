import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logger = logging.getLogger("Status_logger")

error_logger = logging.getLogger("error_logger")

# set loggers level
logger.setLevel(20)
error_logger.setLevel(40)