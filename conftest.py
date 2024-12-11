import pytest
from methods.courier_methods import CourierMethods
from config import COURIER_DATA

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
