import pytest
import requests
from config import Config

names = [("Maksim"),
        ("Jane"),
        ("")]


class TestFirstAPI:

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = Config.API_URL + Config.API_METHOD_HELLO
        data = {"name": name}
        response = requests.get(url=url, params=data)
        assert response.status_code == 200, f"Wrong response code: {response.status_code}"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no 'answer' field in response_dict."

        if name == "":
            expected_response_text = f"Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict['answer']
        assert expected_response_text == actual_response_text, "Actual response text is not correct"


if __name__ == '__main__':

    print(Config.API_URL)
