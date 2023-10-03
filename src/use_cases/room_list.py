from src.responses.responses import ResponseSuccess


def room_list_use_case(repository, request):
    rooms = repository.list()
    return ResponseSuccess(rooms)
