import configparser

config = configparser.RawConfigParser()
config.read("..\\config\\config.ini")


class Read_Config:
    @staticmethod
    def get_app_ur():
        return config.get('common data', 'app_url')

    @staticmethod
    def get_username():
        return config.get('common data', 'username')

    @staticmethod
    def get_password():
        return config.get('common data', 'password')
