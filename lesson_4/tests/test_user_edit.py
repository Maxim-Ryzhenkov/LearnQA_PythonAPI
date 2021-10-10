import json

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(url="/user", data=register_data)
        Assertions.assert_code_status(response1, expected_status_code=200)
        Assertions.assert_json_has_key(response1, name="id")
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, name="id")

        # LOGIN
        login_data = {"email": email,
                      "password": password}
        response2 = MyRequests.post(url="/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, cookie_name="auth_sid")
        token = self.get_header(response2, header_name="x-csrf-token")

        # EDIT
        new_name = "Changed name"
        response3 = MyRequests.put(url=f"/user/{user_id}",
                                   cookies={"auth_sid": auth_sid},
                                   headers={"x-csrf-token": token},
                                   data={"firstName": new_name})
        Assertions.assert_code_status(response3, expected_status_code=200)

        # GET
        response4 = MyRequests.get(url=f"/user/{user_id}",
                                   cookies={"auth_sid": auth_sid},
                                   headers={"x-csrf-token": token})
        Assertions.assert_json_value_by_name(response4,
                                             name="firstName",
                                             expected_value=new_name,
                                             error_message="Wrong name of the user after edit.")
