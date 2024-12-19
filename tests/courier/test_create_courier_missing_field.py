import pytest
import allure
from config import COURIER_DATA, COURIER_RESPONSES
from methods.courier_methods import CourierMethods

@allure.feature('Регистраия курьера при отсутсвии одного поля')
class TestCreateCourierMissingFields:
    @pytest.mark.parametrize(
        "courier_data, missing_field",
        [
            (COURIER_DATA["missing_login"], "login"),
            (COURIER_DATA["missing_password"], "password"),
        ]
    )
    @allure.title('Тест на проверку регистрации курьера при отсутсвии одного поля')
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