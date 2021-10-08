import requests
from config import Config


def first_request():
    payload = {"name": "Maksim"}
    method_url = Config.API_URL + '/hello'
    response = requests.get(url=method_url, params=payload)
    print(response.text)


def task_3():
    name = 'Maks'
    print(f"hello from {name}!")


def task_4():
    response = requests.get(Config.API_URL + '/get_text')
    print(response.text)


if __name__ == '__main__':
    first_request()
    task_3()
    task_4()
