import pytest
import requests
from config import BASE_URL, COURIERS_URL, COURIER_DATA

class TestCannotCreateTwoIdenticalCouriers:
    @pytest.mark.parametrize(
        "courier_data",
        [
            COURIER_DATA["valid_courier"],
            COURIER_DATA["valid_courier"]
        ]
    )
    def test_cannot_create_two_identical_couriers(self, courier_data):
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=courier_data)
        assert response.status_code == 409 and "Этот логин уже используется" in response.json().get("message", ""), (
            f"Expected status 409 for duplicate, but got {response.status_code}. Response: {response.json()}"
        )

