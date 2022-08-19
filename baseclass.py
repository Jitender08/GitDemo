import inspect
import logging

class BaseClass:

    def test_loggingDemo(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger( loggername )
        filehandler = logging.FileHandler("log file.log")
        formatter = logging.Formatter(" %(asctime)s: %(levelname)s: %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
