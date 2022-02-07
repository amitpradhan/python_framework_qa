import logging


class Log_Gen:
    @staticmethod
    def generate_log():
        logging.basicConfig(filename='..\\logs\\automation.log',
                           level=logging.INFO,force=True)
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logging.getLogger()


#