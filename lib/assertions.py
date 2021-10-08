import json
from requests import Response


class Assertions:

    @staticmethod
    def assert_json_value_by_name(response: Response, name: str, expected_value, error_message: str):
        """ Get and assert json value """
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message
