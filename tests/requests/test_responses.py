from src.requests.room_list import RoomListRequest


def test_build_room_list_request_without_parameters():
    # Arrange

    # Act
    request = RoomListRequest()

    # Assert
    assert bool(request) is True


def test_build_room_list_request_from_dict():
    # Arrange

    # Act
    request = RoomListRequest.from_dict({})

    # Assert
    assert bool(request) is True
