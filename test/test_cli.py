from pytest import fixture

from typer.testing import CliRunner

from stateflow.cli import app


@fixture(scope="module")
def runner():
    return CliRunner()


def test_app(runner):
    result = runner.invoke(app, ["say-hi", "test-user"])
    assert result.exit_code == 0
    assert "Hi test-user!" in result.stdout
