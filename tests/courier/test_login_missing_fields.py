import pytest
import allure
from config import COURIER_DATA, COURIER_RESPONSES
from methods.courier_methods import CourierMethods

@allure.feature('Ошибка при отсутсвии одного поля')
class TestLoginMissingFields:
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
        assert response.status_code == 400 and response.json().get("message") == COURIER_RESPONSES["login_insufficient_data"]


