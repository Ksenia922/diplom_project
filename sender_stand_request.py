import pip._vendor.requests
import configuration
import data


def get_order_body():
    return {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-04-06",
        "comment": "Sasuke, come back to Konoha",
        "color": ["BLACK"]
    }

# Функция для создания заказа и проверки статуса ответа


def create_order():
    order_body = get_order_body()
    response = pip._vendor.requests.post(
        f"{configuration.MAIN_URL}{configuration.CREATE_ORDER_URL}", json=order_body)
    return response

# Функция для получения заказа по треку и проверки успешности


def get_order_by_track(track):
    response = pip._vendor.requests.get(
        f"{configuration.MAIN_URL}{configuration.GET_ORDER_WITH_TRACK}?t={track}")
    return response
