import pytest
import allure
from config import COURIER_DATA, COURIER_RESPONSES
from methods.courier_methods import CourierMethods

@allure.feature('Логин курьера')
class TestCourierLogin:
    @allure.title('Тест на проверку логина курьера с валидными данными')
    def test_successful_login_courier(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier(
            COURIER_DATA["valid_courier"]["login"],
            COURIER_DATA["valid_courier"]["password"],
            COURIER_DATA["valid_courier"]["firstName"]
        )
        response = courier_methods.login_courier(
            COURIER_DATA["valid_courier"]["login"],
            COURIER_DATA["valid_courier"]["password"],
        )
        response_json = response.json()
        assert "id" in response_json, f"Response does not contain 'id': {response_json}"

    @pytest.mark.parametrize(
        "courier_data, missing_field",
        [
            (COURIER_DATA["login_with_invalid_login"], "login"),
            (COURIER_DATA["login_with_invalid_password"], "password"),
        ]
    )
    @allure.title('Тест на проверку логина курьера с не валидными данными')
    def test_login_negative(self, courier_data, missing_field):
        courier_methods = CourierMethods()
        response = courier_methods.login_courier(
            courier_data.get("login"),
            courier_data.get("password")
        )
        assert response.status_code == 404 and response.json().get("message") == COURIER_RESPONSES["account_not_found"], (
            f"Expected status code 404 and message 'account_not_found', but got "
            f"status {response.status_code} and response {response.json()}."
        )

    @pytest.mark.parametrize(
        "courier_data, missing_field",
        [
            (COURIER_DATA["login_without_login"], "login"),
            (COURIER_DATA["login_without_password"], "password"),
        ]
    )
    @allure.title('Тест на проверку логина курьера при отсутсвии одного поля')
    def test_login_missing_fields(self, courier_data, missing_field):
        courier_methods = CourierMethods()
        response = courier_methods.login_courier(
            courier_data.get("login"),
            courier_data.get("password")
        )
        assert response.status_code == 400 and response.json().get("message") == COURIER_RESPONSES["login_insufficient_data"], (
            f"Expected status code 400 and message 'login_insufficient_data', but got "
            f"status {response.status_code} and response {response.json()}."
        )
