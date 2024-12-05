BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/"
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

ORDER_DATA_1 = {}
ORDER_DATA_2 = {}

COURIER_DATA = {
    "valid_courier": {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    },
    "missing_login": {
        "password": "ninja",
        "firstName": "saske"
    },
    "duplicate_courier": {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }
}