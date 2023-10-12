from src.responses.responses import (
    ResponseSuccess, ResponseFailure, ResponseTypes, build_response_from_invalid_request)

from src.requests.room_list import RoomListInvalidRequest

SUCCESS_VALUE = {"key": ["value1", "value2"]}
GENERIC_RESPONSE_TYPE = "Response"
GENERIC_RESPONSE_MESSAGE = "This is a response"


def test_response_success_is_true():
    # Act
    response = ResponseSuccess(SUCCESS_VALUE)

    # Assert
    assert bool(response) is True


def test_response_success_is_false():
    # Act
    response = ResponseFailure(GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE)

    # Assert
    assert bool(response) is False


def test_response_success_has_type_and_value():
    # Act
    response = ResponseSuccess(SUCCESS_VALUE)

    # Assert
    assert response.type == ResponseTypes.SUCCESS
    assert response.value == SUCCESS_VALUE


def test_response_failure_has_type_and_message():
    # Act
    response = ResponseFailure(
        GENERIC_RESPONSE_TYPE, GENERIC_RESPONSE_MESSAGE
    )

    # Assert
    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == GENERIC_RESPONSE_MESSAGE
    assert response.value == {
        "type":
        GENERIC_RESPONSE_TYPE,
        "message": GENERIC_RESPONSE_MESSAGE
    }


def test_response_failure_initialization_with_exception():
    # Act
    response = ResponseFailure(
        GENERIC_RESPONSE_TYPE, Exception("Just an error message")
    )

    # Assert
    assert bool(response) is False
    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == "Exception: Just an error message"


def test_response_failure_from_empty_invalid_request():
    # Act
    response = build_response_from_invalid_request(
        RoomListInvalidRequest()
    )

    # Assert
    assert bool(response) is False
    assert response.type == ResponseTypes.PARAMETERS_ERROR


def test_response_failure_from_invalid_request_with_errors():
    # Arrange
    request = RoomListInvalidRequest()
    request.add_error("path", "is mandatory")
    request.add_error("path", "can't be blank")

    # Act
    response = build_response_from_invalid_request(request)

    # Assert
    assert bool(response) is False
    assert response.type == ResponseTypes.PARAMETERS_ERROR
    assert response.message == "path: is mandatory\npath: can't be blank"
