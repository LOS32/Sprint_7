import allure
from methods.courier_methods import CourierMethods
from config import NO_COURIER_ID

@allure.feature('Удаление курьера')
class TestDeleteCourierWithoutId:
    @allure.title('Успешное удаление курьера')
    def test_delete_courier_without_id(self):
        courier_methods = CourierMethods()
        no_courier_id = NO_COURIER_ID
        delete_response = courier_methods.delete_courier(no_courier_id)
        assert delete_response.status_code == 404 and delete_response.json().get(
            "message") == "Not Found.", (
            f"Expected status 404 with message 'Not Found.', got "
            f"status {delete_response.status_code} and response {delete_response.json()}"
        )