import pytest
import requests
from config import Config
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAuth(BaseCase):

    exclude_params = [
        ("no cookies"),
        ("no token")
    ]

    def setup(self):
        data = {"email": "vinkotov@example.com",
                "password": "1234"}
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_auth_from_auth_method = self.get_json_value(response1, "user_id")

    def test_auth_user(self):
        url_user_auth = Config.API_URL + "/user/auth"
        response2 = requests.get(url=url_user_auth,
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            response=response2,
            name="user_id",
            expected_value=self.user_auth_from_auth_method,
            error_message="User id from auth method not equal user id from check method"
        )

    @pytest.mark.parametrize("condition", exclude_params)
    def test_auth_negative_check(self, condition):

        if condition == 'no cookies':
            response2 = requests.get(url=Config.API_URL + "/user/auth",
                                     headers={"x-csrf-token": self.token})
        else:
            response2 = requests.get(url=Config.API_URL + "/user/auth",
                                     cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            response=response2,
            name="user_id",
            expected_value=0,
            error_message=f"User is autorized with condition {condition}"
        )
