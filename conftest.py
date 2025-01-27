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
    courier_id = response.json().get("id") #  courier_id = login_response.json().get("id")
    yield courier_id
    if courier_id:
        CourierMethods().delete_courier(courier_id)

@pytest.fixture()
def courier_and_login():
    courier_data = COURIER_DATA["valid_courier"]
    CourierMethods().create_courier(
        courier_data["login"],
        courier_data["password"],
        courier_data["firstName"]
    )
    login_response = CourierMethods.login_courier(
        courier_data["login"],
        courier_data["password"]
    )
    courier_id = login_response.json().get("id")
    yield courier_id
    delete_response = CourierMethods().delete_courier(courier_id)
    if delete_response.status_code != 200:
        print(f"Failed to delete courier: {delete_response.json()}")



@pytest.fixture()
def order():
    order_methods = OrderMethods()
    order_data = ORDER_DATA["order_data_black"]
    response = order_methods.create_order(order_data)
    order_track = response.json().get("track")
    yield {"order_methods": order_methods, "order_track": order_track}

@pytest.fixture()
def order_id():
    order_methods = OrderMethods()
    order_data = ORDER_DATA["order_data_black"]
    create_response = order_methods.create_order(order_data)
    assert create_response.status_code == 201, f"Failed to create order: {create_response.json()}"
    order_track = create_response.json().get("track")
    get_order_response = order_methods.get_order_by_track(order_track)
    assert get_order_response.status_code == 200, f"Failed to retrieve order by track: {get_order_response.json()}"
    order_id = get_order_response.json()["order"].get("id")
    yield {"order_methods": order_methods, "order_track": order_track, "order_id": order_id}
