import allure
from methods.order_methods import OrderMethods

@allure.feature("Получение заказа по несуществующему номеру")
class TestGetOrderByTrackNonexistentNumber:
    @allure.title("Запрос с несуществующим номером заказа возвращает ошибку")
    def test_get_order_by_track_nonexistent_number(self):
        order_methods = OrderMethods()

    # Используем заведомо несуществующий трекинговый номер
        nonexistent_track_number = 99999999
        response = order_methods.get_order_by_track(nonexistent_track_number)
        response_json = response.json()

    # Проверяем статус-код и сообщение об ошибке
        assert response.status_code == 404 and response_json.get("message") == "Заказ не найден", (
            f"Expected status 404 with 'Заказа с таким id не существует', but got {response.status_code} and {response_json}"
        )