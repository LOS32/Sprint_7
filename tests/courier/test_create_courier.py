from helpers import register_new_courier_and_return_login_password
import requests
from config import BASE_URL, COURIERS_URL

@allure.feature('Регистраия курьера')
class TestCourier:
    @allure.title('Успешная регистрации курьера')
    def test_create_courier(self):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)
        assert response.status_code == 201 and response.json().get("ok") is True, (
            f"Expected status code 201 and 'ok' to be True, but got status {response.status_code} and response {response.json()}"
        )


