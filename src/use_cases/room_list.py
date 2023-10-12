from src.responses.responses import (ResponseSuccess,
                                     ResponseFailure,
                                     ResponseTypes,
                                     build_response_from_invalid_request
                                     )


def room_list_use_case(repository, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        rooms = repository.list(filters=request.filters)
        return ResponseSuccess(rooms)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
