import allure
from methods.courier_methods import CourierMethods
from config import INVALID_COURIER_ID

@allure.feature('Ошибка при удалении курьера')
class TestDeleteCourierWithInvalidId:
    @allure.title("Удаление курьера с несуществующим ID")
    def test_delete_courier_with_invalid_id(self):
        courier_methods = CourierMethods()
        invalid_id = INVALID_COURIER_ID
        delete_response = courier_methods.delete_courier(invalid_id)
        response_json = delete_response.json()
        assert delete_response.status_code == 404 and response_json.get("message") == "Курьера с таким id нет.", (
            f"Expected status 404 with message 'Курьера с таким id нет.', got "
            f"status {delete_response.status_code} and response {response_json}"
        )
