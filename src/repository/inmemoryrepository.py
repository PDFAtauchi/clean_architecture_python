from src.domain.room import Room


class InMemoryRepository:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [Room.from_dict(room) for room in self.data]
