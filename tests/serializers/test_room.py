import json
import uuid

from src.serializers.room import RoomJsonEncoder
from src.domain.room import Room

def test_serialize_domain_room():
    # Arrange
    code = uuid.uuid4()
    size = 200
    price = 10
    longitude = -0.09998975
    latitude = 51.75436293

    room = Room(
        code,
        size,
        price,
        longitude,
        latitude,
    )

    # Act
    expected_json = f"""
    {{
        "code": "{code}",
        "size": {size},
        "price": {price},
        "longitude": {longitude},
        "latitude": {latitude}
    }}
    """

    json_room = json.dumps(room, cls=RoomJsonEncoder)

    # Assert
    assert json.loads(expected_json) == json.loads(json_room)