import logging

class Log:
    def __init__(self, config):
        self.accessLogPath = config["log"]["access_log"]
        self.errorLogPath = config["log"]["error_log"]
  
    def critical(self, logger, message):
        logger.setLevel(logging.CRITICAL)
        logger.critical(message)
        
    def error(self, logger, message):
        logger.setLevel(logging.ERROR)
        logger.error(message)
       
    def warning(self, logger, message):
        logger.setLevel(logging.WARNING)
        logger.warning(message)
        
    def info(self, logger, message):
        logger.setLevel(logging.INFO)
        logger.info(message)
        
    def debug(self, logger, message):
        logger.setLevel(logging.DEBUG)
        logger.debug(message)
        
    def notset(self, logger, message):
        logger.setLevel(logging.NOTSET)
        logger.notset(message)

    def outLogs(self, logger, message, level):
        switcher = {
            1: "critical",
            2: "error",
            3: "warning",
            4: "info",
            5: "debug",
            6: "notset"
        }
        getattr(self, switcher[level])(logger, message)

    def accessLog(self, message, level):
        logger = logging.getLogger("AccessLog")
        filehandler = logging.FileHandler(self.accessLogPath)
        formatter = logging.Formatter('%(asctime)s -- %(levelname)s:%(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        self.outLogs(logger, message, level)

    def errorLog(self, message, level):
        logger = logging.getLogger("ErrorLog")
        filehandler = logging.FileHandler(self.errorLogPath)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        self.outLogs(logger, message, level)
