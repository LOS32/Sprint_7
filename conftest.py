import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
from config import COURIER_DATA
from config import ORDER_DATA

@pytest.fixture()
def courier():
    courier_data = COURIER_DATA["valid_courier"]
    response = CourierMethods().create_courier(
        courier_data["login"],
        courier_data["password"],
        courier_data["firstName"]
    )
    courier_id = response.json().get("id")
    yield courier_id
    if courier_id:
        CourierMethods().delete_courier(courier_id)

@pytest.fixture()
def order():
    order_methods = OrderMethods()
    order_data = ORDER_DATA["order_data_black"]
    response = order_methods.create_order(order_data)
    order_track = response.json().get("track")
    yield {"order_methods": order_methods, "order_track": order_track}