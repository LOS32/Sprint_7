BASE_URL = "https://qa-scooter.praktikum-services.ru"

ENDPOINTS = {
    "create_courier": f"{BASE_URL}/api/v1/courier",
    "login_courier": f"{BASE_URL}/api/v1/courier/login",
    "delete_courier": f"{BASE_URL}/api/v1/courier/{{courier_id}}"
}

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