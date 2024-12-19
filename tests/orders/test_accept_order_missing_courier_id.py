import allure
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods
from config import COURIER_DATA, ORDER_DATA, NO_COURIER_ID, COURIER_RESPONSES


@allure.feature("Принятие заказа")
class TestAcceptOrderMissingCourierId:
    @allure.title("Попытка принять заказ без ID курьера")
    def test_accept_order_missing_courier_id(self):
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
        login_response.json().get("id")
        no_courier_id = NO_COURIER_ID
        order_data = ORDER_DATA["order_data_black"]
        create_order_response = order_methods.create_order(order_data)
        track_number = create_order_response.json().get("track")
        get_order_response = order_methods.get_order_by_track(track_number)
        order_id = get_order_response.json()["order"].get("id")
        accept_order_response = order_methods.accept_order(order_id, no_courier_id)  # Здесь не передаётся ID курьера
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 400 and response_json.get("message") == COURIER_RESPONSES["not_found_data"]



