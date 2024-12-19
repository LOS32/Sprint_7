import allure
from methods.courier_methods import CourierMethods
from config import NO_COURIER_ID, COURIER_RESPONSES

@allure.feature('Ошибка при удалении курьера')
class TestDeleteCourierWithoutId:
    @allure.title('Удаление курьера без ID')
    def test_delete_courier_without_id(self):
        courier_methods = CourierMethods()
        no_courier_id = NO_COURIER_ID
        delete_response = courier_methods.delete_courier(no_courier_id)
        assert delete_response.status_code == 404 and delete_response.json().get("message") == COURIER_RESPONSES["not_found_generic"]