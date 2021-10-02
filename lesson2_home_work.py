import json
import time
import requests
from config import Config


def ex5():
    raw_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
               '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
    parsed_text = json.loads(raw_text)
    print("Упражнение 5 - Парсим строку в JSON")
    print(f'Ответ на задание: {parsed_text.get("messages")[1].get("message")}')


def ex6():
    """ Длинный редирект """
    response = requests.get(Config.API_URL + '/long_redirect', allow_redirects=True)
    responses_history_len = len(response.history)
    final_response = response
    print("\n\nУпражнение 6 - Длинный редирект")
    print(f"Ответ на задание:")
    print(f"Всего редиректов: {responses_history_len}")
    print(f"Кончный URL: {final_response.url}")


def ex7():
    """ Запросы и методы """
    url = Config.API_URL + '/compare_query_type'
    print("\n\nУпражнение 7 - запросы и методы")
    print(f"Ответ на задание:")
    for method in ['GET', 'POST', 'PUT', 'DELETE']:
        response = requests.get(url=url, params={"method": method})
        print(f"requests.get + method: {method}. Result - {response.text}")
        response = requests.post(url=url, data={"method": method})
        print(f"requests.post + method: {method}. Result - {response.text}")
        response = requests.put(url=url, data={"method": method})
        print(f"requests.put + method: {method}. Result - {response.text}")
        response = requests.delete(url=url, data={"method": method})
        print(f"requests.delete + method: {method}. Result - {response.text}")


def ex8():
    """ Токены """
    url = Config.API_URL + '/longtime_job'
    print("\n\nУпражнение 8 - Токены")
    print(f"Ответ на задание:")
    # Create new task
    response = requests.get(url)
    parsed_response = response.json()
    token = parsed_response.get('token')
    seconds = parsed_response.get('seconds')
    print(f"Создана задача с токеном: {token}")
    print(f"Время ожидания: {seconds} сек.")

    # test request 1
    response = requests.get(url, params={'token': token})
    parsed_response = response.json()
    print(parsed_response.get('status'))

    # test request 2
    print(f"I fall asleep for {seconds} seconds")
    time.sleep(seconds)
    response = requests.get(url, params={'token': token})
    parsed_response = response.json()
    print(parsed_response.get('status'))
    print(parsed_response.get('result'))


def ex9():
    """ Подбор пароля """

    def get_auth_cookie(password):
        method_url = Config.API_URL + '/get_secret_password_homework'
        login = "super_admin"
        payload = {"login": login, "password": password}
        response = requests.post(url=method_url, data=payload)
        cookie_value = response.cookies.get('auth_cookie')
        cookie = {'auth_cookie': cookie_value}
        return cookie

    def check_auth_cookie(cookie):
        method_url = Config.API_URL + '/check_auth_cookie'
        response = requests.post(url=method_url, cookies=cookie)
        return response.text

    common_passwords = ['123456', '123456', '123456', 'password', 'password', 'password', 'password',
                        'password', 'password', '456789', '12345678', '12345678', '12345678', '12345',
                        '12345678', '12345', '12345678', '123456789', 'qwerty', 'qwerty', 'abc123', 'qwerty',
                        '12345678', 'qwerty', '12345678', 'qwerty', '12345678', 'password', 'abc123',
                        'qwerty', 'abc123', 'qwerty', '12345', 'football', '12345', '12345', '1234567',
                        'monkey', 'monkey', '123456789', '123456789', '123456789', 'qwerty', '123456789', '111111',
                        '12345678',
                        '1234567', 'letmein', '111111', '1234', 'football', '1234567890', 'letmein', '1234567', '12345',
                        'letmein', 'dragon', '1234567', 'baseball', '1234', '1234567', '1234567', 'sunshine',
                        'iloveyou',
                        'trustno1', '111111', 'iloveyou', 'dragon', '1234567', 'princess', 'football', 'qwerty',
                        '111111',
                        'dragon', 'baseball', 'adobe123', 'football', 'baseball', '1234', 'iloveyou', 'iloveyou',
                        '123123',
                        'baseball', 'iloveyou', '123123', '1234567', 'welcome', 'login', 'admin', 'princess', 'abc123',
                        '111111', 'trustno1', 'admin', 'monkey', '1234567890', 'welcome', 'welcome', 'admin',
                        'qwerty123',
                        'iloveyou', '1234567', '1234567890', 'letmein', 'abc123', 'solo', 'monkey', 'welcome',
                        '1q2w3e4r',
                        'master', 'sunshine', 'letmein', 'abc123', '111111', 'abc123', 'login', '666666', 'admin',
                        'sunshine', 'master', 'photoshop', '111111', '1qaz2wsx', 'admin', 'abc123', 'abc123',
                        'qwertyuiop',
                        'ashley', '123123', '1234', 'mustang', 'dragon', '121212', 'starwars', 'football', '654321',
                        'bailey', 'welcome', 'monkey', 'access', 'master', 'flower', '123123', '123123', '555555',
                        'passw0rd', 'shadow', 'shadow', 'shadow', 'monkey', 'passw0rd', 'dragon', 'monkey', 'lovely',
                        'shadow', 'ashley', 'sunshine', 'master', 'letmein', 'dragon', 'passw0rd', '654321', '7777777',
                        '123123', 'football', '12345', 'michael', 'login', 'sunshine', 'master', '!@#$%^&*', 'welcome',
                        '654321', 'jesus', 'password1', 'superman', 'princess', 'master', 'hello', 'charlie', '888888',
                        'superman', 'michael', 'princess', '696969', 'qwertyuiop', 'hottie', 'freedom', 'aa123456',
                        'princess',
                        'qazwsx', 'ninja', 'azerty', '123123', 'solo', 'loveme', 'whatever', 'donald', 'dragon',
                        'michael', 'mustang', 'trustno1', 'batman', 'passw0rd', 'zaq1zaq1', 'qazwsx', 'password1',
                        'password1',
                        'Football', 'password1', '000000', 'trustno1', 'starwars', 'password1', 'trustno1', 'qwerty123',
                        '123qwe']

    for password in set(common_passwords):
        print(f"Проверяю пароль: {password}")
        cookie = get_auth_cookie(password=password)
        result = check_auth_cookie(cookie)
        print(result)
        if result == "You are authorized":
            print(f"Успешно! Пароль '{password}' подошел.")
            break


if __name__ == "__main__":
    ex5()
    ex6()
    ex7()
    ex8()
    ex9()
