import pytest
import uuid
from unittest import mock

from src.domain.room import Room
from src.use_cases.room_list import room_list_use_case
from src.requests.room_list import build_room_list_request
from src.responses.responses import ResponseTypes


@pytest.fixture
def domain_rooms():
    room1 = Room(
        code=uuid.uuid4(),
        size=200,
        price=50,
        longitude=-0.099999,
        latitude=51.2222
    )

    room2 = Room(
        code=uuid.uuid4(),
        size=250,
        price=55,
        longitude=-0.099999,
        latitude=51.2222
    )

    room3 = Room(
        code=uuid.uuid4(),
        size=300,
        price=60,
        longitude=-0.099999,
        latitude=51.2222
    )

    room4 = Room(
        code=uuid.uuid4(),
        size=350,
        price=65,
        longitude=-0.099999,
        latitude=51.2222
    )

    return [room1, room2, room3, room4]


def test_room_list_without_parameters(domain_rooms):
    # Arrange
    repository = mock.Mock()
    repository.list.return_value = domain_rooms

    # Act
    request = build_room_list_request()
    response = room_list_use_case(repository, request)

    # Assert
    assert bool(response) is True
    repository.list.assert_called_with(filters=None)
    assert domain_rooms == response.value


def test_room_list_with_filters(domain_rooms):
    # Arrange
    repository = mock.Mock()
    repository.list.return_value = domain_rooms

    # Act
    query_filters = {"code__eq": 5}
    request = build_room_list_request(filters=query_filters)
    response = room_list_use_case(repository, request)

    # Assert
    assert bool(response) is True
    repository.list.assert_called_with(filters=query_filters)
    assert response.value == domain_rooms


def test_room_list_handles_generic_error():
    # Arrange
    repository = mock.Mock()
    repository.list.side_effect = Exception("Just an error message")

    # Act
    request = build_room_list_request(filters={})
    response = room_list_use_case(repository, request)

    # Assert
    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message"
    }


def test_room_list_handles_bad_request():
    # Arrange
    repository = mock.Mock()

    # Act
    request = build_room_list_request(filters=5)
    response = room_list_use_case(repository, request)

    # Assert
    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable"
    }
