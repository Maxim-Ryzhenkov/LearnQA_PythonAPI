import requests


def first_request():
    response = requests.get('https://playground.learnqa.ru/api/hello')
    print(response.text)


def task_3():
    name = 'Maks'
    print(f"hello from {name}!")


def task_4():
    response = requests.get('https://playground.learnqa.ru/api/get_text')
    print(response.text)


if __name__ == '__main__':
    first_request()
    task_3()
    task_4()
