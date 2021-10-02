import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class Config:
    API_URL = config["urls"]["api_url"]
    API_METHOD_MAP = config["urls"]["method_map"]
    API_METHOD_HELLO = config["urls"]["method_hello"]
