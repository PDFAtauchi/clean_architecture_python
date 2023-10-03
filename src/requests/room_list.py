class RoomListRequest:
    @classmethod
    def from_dict(cls, data_dict):
        return cls()

    def __bool__(self):
        return True
