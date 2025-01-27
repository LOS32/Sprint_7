import allure
import pytest
from helpers import register_new_courier_and_return_login_password
from methods.courier_methods import CourierMethods
from config import COURIER_DATA, COURIER_RESPONSES

@allure.feature('Регистрация курьера')
class TestCourier:
    @allure.title('Успешная регистрация курьера')
    def test_successful_create_courier(self):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        courier_methods = CourierMethods()
        response = courier_methods.create_courier(payload["login"], payload["password"], payload["firstName"])
        assert response.status_code == 201 and response.json().get("ok") is True, (
            f"Expected status code 201 and 'ok' to be True, but got status {response.status_code} and response {response.json()}"
        )

    @allure.title('Регистрация двух курьеров с одинаковыми данными')
    def test_cannot_create_two_identical_couriers(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier(
            COURIER_DATA["valid_courier"]["login"],
            COURIER_DATA["valid_courier"]["password"],
            COURIER_DATA["valid_courier"]["firstName"]
        )
        duplicate_response = courier_methods.create_courier(
            COURIER_DATA["duplicate_courier"]["login"],
            COURIER_DATA["duplicate_courier"]["password"],
            COURIER_DATA["duplicate_courier"]["firstName"]
        )
        assert duplicate_response.status_code == 409 and duplicate_response.json().get("message") == COURIER_RESPONSES["duplicate_courier"]

    @pytest.mark.parametrize(
        "courier_data, missing_field",
        [
            (COURIER_DATA["missing_login"], "login"),
            (COURIER_DATA["missing_password"], "password"),
        ]
    )
    @allure.title('Регистрация курьера при отсутствии обязательного поля')
    def test_create_courier_missing_field(self, courier_data, missing_field):
        courier_methods = CourierMethods()
        response = courier_methods.create_courier(
            courier_data.get("login"),
            courier_data.get("password"),
            courier_data.get("firstName")
        )
        assert response.status_code == 400 and response.json().get("message") == COURIER_RESPONSES[
            "insufficient_data"], (
            f"Expected 400 with message '{COURIER_RESPONSES['insufficient_data']}', but got "
            f"status {response.status_code} and response {response.json()}"
        )
