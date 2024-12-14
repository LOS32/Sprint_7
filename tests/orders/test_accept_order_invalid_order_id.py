import allure
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods
from config import COURIER_DATA, ORDER_DATA, INVALID_ORDER_ID

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
        courier_id = login_response.json().get("id")
        order_data = ORDER_DATA["order_data_black"]
        create_order_response = order_methods.create_order(order_data)
        track_number = create_order_response.json().get("track")
        order_methods.get_order_by_track(track_number)
        invalid_order_id = INVALID_ORDER_ID
        accept_order_response = order_methods.accept_order(invalid_order_id, courier_id)
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 404 and response_json.get(
            "message") == "Заказа с таким id не существует", (
            f"Expected status 404 with 'Заказа с таким id не существует', but got {accept_order_response.status_code} and {response_json}"
        )