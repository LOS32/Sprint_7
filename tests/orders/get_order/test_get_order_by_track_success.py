import allure
from methods.order_methods import OrderMethods
from config import ORDER_DATA

@allure.feature("Получение заказа по номеру")
class TestGetOrderByTrackSuccess:
    @allure.title("Успешное получение заказа по трекинговому номеру")
    def test_get_order_by_track_success(self):
        order_methods = OrderMethods()
        create_order_response = order_methods.create_order(ORDER_DATA["order_data_black"])
        track_number = create_order_response.json().get("track")
        get_order_response = order_methods.get_order_by_track(track_number)
        response_json = get_order_response.json()
        assert get_order_response.status_code == 200 and "order" in response_json, (
            f"Expected status 200 with 'order' in response, but got {get_order_response.status_code} and {response_json}"
        )

