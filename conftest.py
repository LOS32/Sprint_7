import pytest

from methods.order_methods import OrderMethods, response

@pytest.fixture()
def courier():
    response = CourierMethods.create.courier(COURIER_NAME)
    yeld response.json()['id']
    CourierMethods.delete_courier(response.json()['id'])