import allure
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods
from config import COURIER_DATA, ORDER_DATA, NO_ORDER_ID

@allure.feature("Принятие заказа")
class TestAcceptOrderMissingOrderId:
    @allure.title("Попытка принять заказ без ID заказа")
    def test_accept_order_missing_order_id(self):
        order_methods = OrderMethods()
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
        order_data = ORDER_DATA["order_data_black"]
        create_order_response = order_methods.create_order(order_data)
        track_number = create_order_response.json().get("track")
        get_order_response = order_methods.get_order_by_track(track_number)
        get_order_response.json()["order"].get("id")
        no_order_id = NO_ORDER_ID
        accept_order_response = order_methods.accept_order(no_order_id, courier_id)
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 404 and response_json.get("message") == "Not Found.", (
            f"Expected status 404 with 'Not Found.', but got {accept_order_response.status_code} and {response_json}"
        )