import pytest
import sender_stand_request

# Тест 1. Создание заказа и получение по треку
# Ксения Пискунова, 28-я когорта — Финальный проект. Инженер по тестированию плюс


def test_create_order_and_get_by_track_positive():
    create_response = sender_stand_request.create_order()
    track = create_response.json()["track"]
    track_response = sender_stand_request.get_order_by_track(track)
    assert track_response.status_code == 200
