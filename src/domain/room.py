import uuid
import dataclasses


@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)

    def to_dict(self):
        return dataclasses.asdict(self)
