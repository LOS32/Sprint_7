import pytest
import requests
from config import BASE_URL, COURIERS_URL, COURIER_DATA


class TestCreateCourierMissingFields:
    @pytest.mark.parametrize(
        "courier_data, missing_field",
        [
            (COURIER_DATA["missing_login"], "login"),
            (COURIER_DATA["missing_password"], "password"),
        ]
    )
    def test_create_courier_missing_field(self, courier_data, missing_field):
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=courier_data)
        assert response.status_code == 400 and response.json().get("message") == "Недостаточно данных для создания учетной записи"
