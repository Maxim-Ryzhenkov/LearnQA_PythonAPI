import allure
from allure_commons.types import AttachmentType
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.image import Image


@allure.feature("Получение данных пользователя")
class TestUserGet(BaseCase):

    @allure.story("Получение данных неавторизованного пользователя")
    def test_get_user_details_not_aut(self):
        response = MyRequests.get(url="/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_keys(response, names=["email", "firstName", "lastName"])
        allure.attach(Image.get_screenshot_as_byte_array(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.story("Получение данных авторизованного пользователя")
    def test_get_user_details_aut_as_same_user(self):
        data = {"email": "vinkotov@example.com",
                "password": "1234"}
        response1 = MyRequests.post(url="/user/login", data=data)
        auth_sid = self.get_cookie(response1, cookie_name="auth_sid")
        token = self.get_header(response1, header_name="x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, name="user_id")
        #allure.attach(response1.json(), name="Response1 JSON")
        allure.attach(Image.get_screenshot_as_byte_array(), name="Screenshot_1", attachment_type=allure.attachment_type.PNG)

        response2 = MyRequests.get(url=f"/user/{user_id_from_auth_method}",
                                   cookies={"auth_sid": auth_sid},
                                   headers={"x-csrf-token": token})
        Assertions.assert_json_has_keys(response2, names=["username",
                                                          "email",
                                                          "firstName",
                                                          "lastName"])
        #allure.attach(response1.json(), name="Response2 JSON", attachment_type=AttachmentType.JSON)
        allure.attach(Image.get_screenshot_as_byte_array(), name="Screenshot_2", attachment_type=allure.attachment_type.PNG)
