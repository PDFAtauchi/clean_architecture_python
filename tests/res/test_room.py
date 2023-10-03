import json
from unittest import mock

from src.domain.room import Room

room_dict = {
    "code": "3251a5bd-86be-428d-8ae9-6e51a8048c33",
    "size": 200,
    "price": 10,
    "longitude": -0.09998975,
    "latitude": 51.75436293,
}

rooms = [Room.from_dict(room_dict)]


@mock.patch("application.rest.room.room_list_use_case")
def test_get(mock_use_case, client):
    # Arrange
    mock_use_case.return_value = rooms

    # Act
    response = client.get("/rooms")

    # Assert
    expected = json.loads(response.data.decode("UTF-8"))
    assert [room_dict] == expected
    mock_use_case.assert_called()
    assert 200 == response.status_code
    assert "application/json" == response.mimetype
