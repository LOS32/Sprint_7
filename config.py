BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/"
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

ORDER_DATA_1 = {}
ORDER_DATA_2 = {}

COURIER_DATA = {
    "valid_courier": {
        "login": "ninjа",
        "password": "1234",
        "firstName": "saske"
    },
    "missing_login": {
        "password": "1234",
        "firstName": "saske"
    },
    "missing_password": {
        "login": "linjn",
        "firstName": "saske"
    },
    "duplicate_courier": {
        "login": "naygd",
        "password": "1234",
        "firstName": "saske"
    },
    "login_without_password": {
        "login": "ninjа",
        "password": ""
    },
    "login_without_login": {
        "login": "",
        "password": "1234"
    },
}