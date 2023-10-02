import pytest
import uuid
from unittest import mock

from src.domain.room import Room
from src.use_cases.room_list import room_list_use_case

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
    result = room_list_use_case(repository)

    # Assert
    repository.list.assert_called_with()
    assert domain_rooms == result

