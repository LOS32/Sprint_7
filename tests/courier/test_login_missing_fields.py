import pytest
from config import COURIER_DATA
from methods.courier_methods import CourierMethods


class TestLoginMissingFields:
    @pytest.mark.parametrize(
        "courier_data, missing_field",
        [
            (COURIER_DATA["login_without_login"], "login"),
            (COURIER_DATA["login_without_password"], "password"),
        ]
    )
    def test_login_missing_field(self, courier_data, missing_field):
        courier_methods = CourierMethods()
        response = courier_methods.login_courier(
            courier_data.get("login"),
            courier_data.get("password")
        )
        assert response.status_code == 400 and response.json().get("message") == "Недостаточно данных для входа", \
            f"Expected 400 and 'Недостаточно данных для входа', got {response.status_code} and {response.json()}"




