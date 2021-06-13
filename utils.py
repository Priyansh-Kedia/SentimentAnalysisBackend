import configparser

config = configparser.ConfigParser()

config.read('.env')

class Util:
    @staticmethod
    def get_config(config_name):
        return config.get("CONFIG",config_name)