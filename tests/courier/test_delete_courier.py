import allure
from methods.courier_methods import CourierMethods
from config import COURIER_DATA, NO_COURIER_ID, INVALID_COURIER_ID, COURIER_RESPONSES

@allure.feature('Удаление курьера')
class TestDeleteCourier:
    @allure.title('Успешное удаление курьера')
    def test_successful_delete_courier(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier(
            COURIER_DATA["valid_courier"]["login"],
            COURIER_DATA["valid_courier"]["password"],
            COURIER_DATA["valid_courier"]["firstName"]
        )
        login_response = courier_methods.login_courier(
            COURIER_DATA["valid_courier"]["login"],
            COURIER_DATA["valid_courier"]["password"],
        )
        courier_id = login_response.json().get("id")
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 200 and delete_response.json().get("ok") is True, (
            f"Expected status code 200 and 'ok' to be True, but got "
            f"status {delete_response.status_code} and response {delete_response.json()}."
        )

    @allure.title('Удаление курьера без ID')
    def test_delete_courier_without_id(self):
        courier_methods = CourierMethods()
        no_courier_id = NO_COURIER_ID
        delete_response = courier_methods.delete_courier(no_courier_id)
        assert delete_response.status_code == 404 and delete_response.json().get("message") == COURIER_RESPONSES["not_found_generic"], (
            f"Expected status code 404 and message '{COURIER_RESPONSES['not_found_generic']}', but got "
            f"status {delete_response.status_code} and response {delete_response.json()}."
        )

    @allure.title("Удаление курьера с несуществующим ID")
    def test_delete_courier_with_invalid_id(self):
        courier_methods = CourierMethods()
        invalid_id = INVALID_COURIER_ID
        delete_response = courier_methods.delete_courier(invalid_id)
        response_json = delete_response.json()
        assert delete_response.status_code == 404 and response_json.get("message") == COURIER_RESPONSES["not_found"], (
            f"Expected status code 404 and message '{COURIER_RESPONSES['not_found']}', but got "
            f"status {delete_response.status_code} and response {response_json}."
        )


