from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post(url="/user", data=data)
        Assertions.assert_code_status(response, expected_status_code=200)
        Assertions.assert_json_has_key(response, name="id")

    def test_create_user_with_existing_email(self):
        data = self.prepare_registration_data(email="vinkotov@example.com")
        response = MyRequests.post(url="/user", data=data)
        Assertions.assert_code_status(response, expected_status_code=400)
        assert response.content.decode("utf8") == f"Users with email '{data['email']}' already exists", \
            f"Unexpected content {response.content.decode('utf8')}"
