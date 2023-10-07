import logging


"""
Levels of Logging:
Debug -> INFO -> ERROR -> WARNNING -> CRITICAL.
Can change the level to level = logging.INFO, , Logging.WARNING , Logging.ERROR, Logging.CRITICAL
"""
logging.basicConfig(level = logging.DEBUG, filename = "log.log", filemode = 'w' ,format = '%(asctime)s - %(levelname)s - %(message)s') 


logging.debug("This is the first level")
logging.info("This is the second level")
logging.warning("third level")
logging.error("Fourth level")
logging.critical("fifth level")


try:
    1/0
except ZeroDivisionError as e:
    #logging.error(f"Error occured is {e}")
    logging.exception("The error occured")


# Custom logger.


# Grabs the logger of module's name 
logger = logging.getLogger(__name__)

# Setting the directory & file name 
handler = logging.FileHandler("test.log")

# Setting the formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Attaching the formatter to the handler.
handler.setFormatter(formatter)

# Attaching the handler to the logger
logger.addHandler(handler)

# Testing our logger.
logger.info("test the custom logger.")