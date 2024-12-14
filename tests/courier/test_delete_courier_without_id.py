import allure
from methods.courier_methods import CourierMethods

@allure.feature('Удаление курьера')
class TestDeleteCourier:
    @allure.title('Успешное удаление курьера')
    def test_successful_delete_courier(self):
        courier_methods = CourierMethods()
        delete_response = courier_methods.delete_courier(courier_id)
        assert delete_response.status_code == 400 and delete_response.json().get(
            "message") == "Недостаточно данных для удаления курьера", (
            f"Expected status 400 with message 'Недостаточно данных для удаления курьера', got "
            f"status {delete_response.status_code} and response {delete_response.json()}"
        )