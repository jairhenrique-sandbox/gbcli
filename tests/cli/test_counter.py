from typer.testing import CliRunner
from gbcli.cli import app
from unittest import mock

runner = CliRunner()


def test_should_return_a_valid_response():
    result = runner.invoke(app, ["counter", "3"])

    assert result.exit_code == 0
    assert result.stdout == "Contando 1\nContando 2\nContando 3\n"


def test_should_call_loggers_with_correct_message(mock_logger_factory, fake_logger):
    result = runner.invoke(app, ["counter", "3"])

    assert mock_logger_factory.call_args_list == [mock.call("dummy")]
    assert fake_logger.warning.call_args_list == [mock.call("Contando até 3")]
    assert result.exit_code == 0
    assert result.stdout == "Contando 1\nContando 2\nContando 3\n"
