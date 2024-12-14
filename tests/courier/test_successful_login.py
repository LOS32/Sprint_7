import allure
from config import COURIER_DATA
from methods.courier_methods import CourierMethods
from conftest import courier

@allure.feature('Логин курьера')
class TestSuccessfulLogin:
    @allure.title('Тест на проверку логина курьера с валидными данными')
    def test_successful_login(self, courier):
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


