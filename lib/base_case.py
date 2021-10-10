import json.decoder
from requests import Response
from datetime import datetime


class BaseCase:

    def get_cookie(self, response: Response, cookie_name: str) -> str:
        """ Get cookie from response """
        assert cookie_name in response.cookies, f"There not cookie with the name {cookie_name} in the last response"
        return response.cookies.get(cookie_name)

    def get_header(self, response: Response, header_name: str) -> str:
        """ Get header from response """
        assert header_name in response.headers, f"There not header with the name {header_name} in the last response"
        return response.headers.get(header_name)

    def get_json_value(self, response: Response, name: str):
        """ Get json value """
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response not in JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        if not email:
            base_part = "learnqa"
            random_part = f"{datetime.now().strftime('%m%d%Y%H%M%S')}"
            domain = 'example.com'
            email = f"{base_part}{random_part}@{domain}"
        return {"password": "123",
                "username": "learnqa",
                "firstName": "learnqa",
                "lastName": "learnqa",
                "email": email}
