BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/"
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

ORDER_DATA = {
    "order_data_black": {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    },
    "order_data_grey": {
        "firstName": "Sakura",
        "lastName": "Haruno",
        "address": "Konoha, 143 apt.",
        "metroStation": 2,
        "phone": "+7 900 456 78 90",
        "rentTime": 3,
        "deliveryDate": "2020-06-10",
        "comment": "Naruto, stop eating ramen!",
        "color": ["GREY"]
    },
    "order_data_no_color": {
        "firstName": "Kakashi",
        "lastName": "Hatake",
        "address": "Konoha, 144 apt.",
        "metroStation": 1,
        "phone": "+7 700 111 22 33",
        "rentTime": 7,
        "deliveryDate": "2020-06-15",
        "comment": "Team 7 assemble!",
        "color": []
    },
    "order_data_two_colors": {
        "firstName": "Kakashi",
        "lastName": "Hatake",
        "address": "Konoha, 144 apt.",
        "metroStation": 1,
        "phone": "+7 700 111 22 33",
        "rentTime": 7,
        "deliveryDate": "2020-06-15",
        "comment": "Team 7 assemble!",
        "color": ["GREY", "BLACK"]
    },
}

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
    "login_with_invalid_login": {
        "login": "ninva",
        "password": "1234"
    },
    "login_with_invalid_password": {
        "login": "ninja",
        "password": "4321"
    },
}

INVALID_ORDER_ID = 3633333
INVALID_COURIER_ID = 123456789
NO_COURIER_ID = ""
NO_ORDER_ID = ""

COURIER_RESPONSES = {
    "duplicate_courier": "Этот логин уже используется. Попробуйте другой.",
    "insufficient_data": "Недостаточно данных для создания учетной записи",
    "not_found": "Курьера с таким id нет.",
    "account_not_found": "Учетная запись не найдена",
    "login_insufficient_data": "Недостаточно данных для входа",
    "not_found_generic": "Not Found.",
    "courier_id_not_found": "Курьера с таким id не существует",
    "order_not_found": "Заказа с таким id не существует",
    "not_found_data": "Недостаточно данных для поиска",
    "not_found_number_order": "Заказ не найден"
}
