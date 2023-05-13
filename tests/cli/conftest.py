import pytest
from unittest import mock


@pytest.fixture
def fake_logger():
    return mock.Mock()


@pytest.fixture
def mock_logger_factory(fake_logger):
    with mock.patch(
        "gbcli.cli.LoggerFactory.create",
        return_value=fake_logger,
    ) as mock_logger:
        yield mock_logger
