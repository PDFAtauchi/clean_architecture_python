import uuid
from src.domain.room import Room

def test_room_model_init():
    # Arrange
    code = uuid.uuid4()
    size = 200
    price = 10
    longitude = -0.09998975
    latitude = 51.75436293

    # Act
    room = Room(
        code,
        size,
        price,
        longitude,
        latitude,
    )

    # Assert
    assert code == room.code
    assert size == room.size
    assert price == room.price
    assert longitude == room.longitude
    assert latitude == room.latitude


def test_room_model_from_dict():
    # Arrange
    code = uuid.uuid4()
    size = 200
    price = 10
    longitude = -0.09998975
    latitude = 51.75436293

    init_dict = {
        "code": code,
        "size": size,
        "price": price,
        "longitude": longitude,
        "latitude": latitude,
    }

    # Act
    room = Room.from_dict(init_dict)

    # Assert
    assert code == room.code
    assert size == room.size
    assert price == room.price
    assert longitude == room.longitude
    assert latitude == room.latitude

def test_room_model_to_dict():
    # Arrange
    code = uuid.uuid4()
    size = 200
    price = 10
    longitude = -0.09998975
    latitude = 51.75436293

    expected_dict = {
        "code": code,
        "size": size,
        "price": price,
        "longitude": longitude,
        "latitude": latitude,
    }

    # Act
    room = Room(
        code,
        size,
        price,
        longitude,
        latitude,
    )

    # Assert
    actual_dict = room.to_dict()
    assert expected_dict == actual_dict

def test_room_model_comparison():
    # Arrange
    code = uuid.uuid4()
    size = 200
    price = 10
    longitude = -0.09998975
    latitude = 51.75436293

    init_dict = {
        "code": code,
        "size": size,
        "price": price,
        "longitude": longitude,
        "latitude": latitude,
    }

    # Act
    room1 = Room(
        code,
        size,
        price,
        longitude,
        latitude,
    )

    room2 = Room(
        code,
        size,
        price,
        longitude,
        latitude,
    )

    # Assert
    assert room1 == room2
