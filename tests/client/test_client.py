from gbcli.client import get_data
from unittest import mock
import pytest


@pytest.fixture
def mock_client():
    with mock.patch("gbcli.client.client") as mock_client:
        yield mock_client


def test_should_call_get_with_requested_url(mock_client):
    get_data("http://example.com")

    assert mock_client.get.call_args_list == [mock.call("http://example.com")]


def test_should_return_json_data(mock_client):
    mock_client.get.return_value.json.return_value = {"key": "value"}

    response = get_data("http://example.com")

    assert response == {"key": "value"}
