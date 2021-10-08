import os
import configparser

current_dir = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(current_dir, 'config.ini'))


class Config:
    API_URL = config["urls"]["api_url"]
    API_METHOD_MAP = config["urls"]["method_map"]
    API_METHOD_HELLO = config["urls"]["method_hello"]

