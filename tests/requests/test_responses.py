from src.requests.room_list import build_room_list_request

import pytest


def test_build_room_list_request_without_parameters():
    # Arrange

    # Act
    request = build_room_list_request()

    # Assert
    assert request.filters is None
    assert bool(request) is True


def test_build_room_list_request_with_empty_filters():
    # Arrange

    # Act
    request = build_room_list_request({})

    # Assert
    assert {} == request.filters
    assert bool(request) is True


def test_build_room_list_request_with_invalid_filters_parameter():
    # Arrange

    # Act
    request = build_room_list_request(filters=5)

    # Assert
    assert request.has_errors()
    assert "filters" == request.errors[0]["parameter"]
    assert bool(request) is False


def test_build_room_list_request_with_incorrect_filter_keys():
    # Arrange

    # Act
    request = build_room_list_request(filters={"a": 1})

    # Assert
    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False


@pytest.mark.parametrize(
    "key", ["code__eq", "price__eq", "price__lt", "price__gt"]
)
def test_build_room_list_request_accepted_filters(key):
    # Arrange
    filters = {key: 1}

    # Act
    request = build_room_list_request(filters=filters)

    # Assert
    assert request.filters == filters
    assert bool(request) is True


@pytest.mark.parametrize("key", ["code__lt", "code__gt"])
def test_build_room_list_request_rejected_filters(key):
    # Arrange
    filters = {key: 1}

    # Act
    request = build_room_list_request(filters=filters)

    # Assert
    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False
