import requests
import allure
from helpers import register_new_courier_and_return_login_password
from config import BASE_URL, COURIERS_URL
from methods.courier_methods import CourierMethods

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
        courier_methods = CourierMethods()
        response = courier_methods.create_courier(payload["login"], payload["password"], payload["firstName"])
        assert response.status_code == 201 and response.json().get("ok") is True, (
            f"Expected status code 201 and 'ok' to be True, but got status {response.status_code} and response {response.json()}"
        )



