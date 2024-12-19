import allure
from methods.order_methods import OrderMethods
from config import COURIER_RESPONSES

@allure.feature("Получение заказа по несуществующему номеру")
class TestGetOrderByTrackNonexistentNumber:
    @allure.title("Запрос с несуществующим номером заказа возвращает ошибку")
    def test_get_order_by_track_nonexistent_number(self):
        order_methods = OrderMethods()
        nonexistent_track_number = 99999999
        response = order_methods.get_order_by_track(nonexistent_track_number)
        response_json = response.json()
        assert response.status_code == 404 and response_json.get("message") == COURIER_RESPONSES["not_found_number_order"]