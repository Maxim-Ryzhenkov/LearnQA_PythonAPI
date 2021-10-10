import json
import requests
import allure
from lib.logger import Logger
from config import Config


class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"Выполнить POST запрос на ur: {url}"):
            return MyRequests._send(url, data, headers, cookies, "POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"Выполнить GET запрос на ur: {url}"):
            return MyRequests._send(url, data, headers, cookies, "GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"Выполнить PUT запрос на ur: {url}"):
            return MyRequests._send(url, data, headers, cookies, "PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"Выполнить DELETE запрос на ur: {url}"):
            return MyRequests._send(url, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):

        url = f"{Config.API_URL}{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url=url, data=data, headers=headers, cookies=cookies, method=method)

        if method == "GET":
            response = requests.get(url=url, headers=headers, cookies=cookies, params=data)
        elif method == "POST":
            response = requests.post(url=url, headers=headers, cookies=cookies, data=data)
        elif method == "PUT":
            response = requests.put(url=url, headers=headers, cookies=cookies, data=data)
        elif method == "DELETE":
            response = requests.delete(url=url, headers=headers, cookies=cookies, data=data)
        else:
            raise ValueError(f"Bad HTTP method '{method}' was received.")

        allure.attach(json.dumps(headers), name="Request headers", attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(cookies), name="Request cookies", attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(data), name="Request data", attachment_type=allure.attachment_type.JSON)

        Logger.add_response(response)

        allure.attach(str(response.status_code), name="Response status code",
                      attachment_type=allure.attachment_type.TEXT)
        try:
            response_as_dict = response.json()
            allure.attach(json.dumps(response_as_dict), name="Response JSON data",
                          attachment_type=allure.attachment_type.JSON)
        except json.decoder.JSONDecodeError:
            allure.attach(response.text, name="Response content",
                          attachment_type=allure.attachment_type.TEXT)

        return response
