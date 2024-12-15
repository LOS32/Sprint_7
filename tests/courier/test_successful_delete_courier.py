import allure
from methods.courier_methods import CourierMethods
from helpers import register_new_courier_and_return_login_password

@allure.feature('Удаление курьера')
class TestSuccessfulDeleteCourier:
    @allure.title('Успешное удаление курьера')
    def test_successful_delete_courier(self):
        courier_methods = CourierMethods()
        courier_data = register_new_courier_and_return_login_password()
        courier_methods.create_courier(
            courier_data[0],  # login
            courier_data[1],  # password
            courier_data[2]  # firstName
        )
        login_response = courier_methods.login_courier(
            courier_data[0],  # login
            courier_data[1]  # password
        )
        courier_id = login_response.json().get("id")
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200 and delete_response.json().get("ok") is True, (
            f"Expected status code 200 and 'ok' to be True, but got "
            f"status {delete_response.status_code} and response {delete_response.json()}."
        )

