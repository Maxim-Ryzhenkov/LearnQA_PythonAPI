import json

import requests
from json.decoder import JSONDecodeError
from config import Config


def hello():
    payload = {"name": "Maksim"}
    method_url = Config.API_URL + '/hello'
    response = requests.get(url=method_url, params=payload)
    print(response.text)


def get_text():
    response = requests.get(url=Config.API_URL + '/get_text')
    print(response.text)
    try:
        parsed_response_text = response.json()
        print(parsed_response_text)
    except JSONDecodeError:
        print("Response in not a JSON format.")


def get_301():
    response = requests.get(Config.API_URL + '/get_301', allow_redirects=True)
    responses_history_len = len(response.history)
    first_response = response.history[0]
    second_response = response
    print(f"History length: {responses_history_len}")
    print(first_response.url)
    print(first_response.status_code)
    print(second_response.url)
    print(second_response.status_code)


def get_auth_cookie():
    payload = {"password": "secret_pass", "login": "secret_login"}
    method_url = Config.API_URL + '/get_auth_cookie'
    response = requests.post(url=method_url, data=payload)
    print(response.text)
    print(response.status_code)
    cookie_value = response.cookies.get('auth_cookie')
    cookie = {'auth_cookie': cookie_value}
    print(cookie)
    print(response.headers)
    print(json.dumps(dict(response.headers), indent=4))
    return cookie


def check_auth_cookie(cookie):
    method_url = Config.API_URL + '/check_auth_cookie'
    response = requests.post(url=method_url, cookies=cookie)
    print(response.text)
    print(response.status_code)


if __name__ == '__main__':

    cookie = get_auth_cookie()
    check_auth_cookie(cookie)
