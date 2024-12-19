import allure
from config import NO_COURIER_ID, COURIER_RESPONSES
from conftest import courier_and_login, order


@allure.feature("Принятие заказа")
class TestAcceptOrderMissingCourierId:
    @allure.title("Попытка принять заказ без ID курьера")
    def test_accept_order_missing_courier_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        order_track = order["order_track"]
        no_courier_id = NO_COURIER_ID
        get_order_response = order_methods.get_order_by_track(order_track)
        order_id = get_order_response.json()["order"].get("id")
        accept_order_response = order_methods.accept_order(order_id, no_courier_id)
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 400 and response_json.get("message") == COURIER_RESPONSES["not_found_data"]



