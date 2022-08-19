import logging # package

def test_loggingDemo():
    logger = logging.getLogger(__name__) # to log everything
    filehandler = logging.FileHandler("log file.log")# file handler is file location/name
    formatter= logging.Formatter(" %(asctime)s: %(levelname)s: %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    # addhandler will handle file (filehandler) & format in which log level will be printed

    logger.setLevel(logging.WARNING)
    logger.debug("A debug statement is executed") # will only print msg
    logger.info("information statement")# will only print msg
    logger.warning("something is in warning mode")# will only print msg
    logger.error("error message")# will only print msg
    logger.critical("critical issue")# will only print msg


