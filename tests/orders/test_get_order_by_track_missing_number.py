import allure
from methods.order_methods import OrderMethods

@allure.feature("Получение заказа по номеру")
class TestGetOrderByTrackMissingNumber:
    @allure.title("Запрос без номера заказа возвращает ошибку")
    def test_get_order_by_track_missing_number(self):
        order_methods = OrderMethods()
        response = order_methods.get_order_by_track("")
        response_json = response.json()
        assert response.status_code == 400 and response_json.get("message") == "Недостаточно данных для поиска", (
            f"Expected status 400 with 'Недостаточно данных для поиска', but got {response.status_code} and {response_json}"
        )