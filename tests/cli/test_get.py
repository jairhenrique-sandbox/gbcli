import pytest
from typer.testing import CliRunner
from gbcli.cli import app
from unittest import mock

runner = CliRunner()


@pytest.fixture(autouse=True)
def mock_get():
    with mock.patch("gbcli.cli.get_data") as get_data:
        get_data.return_value = {"a": "b"}
        yield get_data


def test_should_return_a_valid_response():
    result = runner.invoke(app, ["get", "https://example.com"])

    assert result.exit_code == 0
    assert result.stdout == ""


def test_should_call_loggers_with_correct_message(
    mock_logger_factory, fake_logger, mock_get
):
    url = "https://example.com"

    result = runner.invoke(app, ["get", url])

    assert mock_logger_factory.call_args_list == [mock.call("dummy")]

    assert fake_logger.info.call_args_list == [
        mock.call(f"Buscando dados na url {url}")
    ]
    assert fake_logger.debug.call_args_list == [
        mock.call(f"Debug response: {mock_get.return_value}")
    ]
    assert result.exit_code == 0
    assert result.stdout == ""
