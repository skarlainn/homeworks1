from typing import Any
import pytest
from src.decorators import log

@log()
def function_success(x: int, y: int) -> int:
    return x + y


@log()
def function_error() -> None:
    raise ValueError("Test error")


def test_log_success(capsys: Any) -> None:
    function_success(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "function_success - ok\n"


def test_log_error(capsys: Any) -> None:
    with pytest.raises(Exception, match="Test error"):
        function_error()

    captured = capsys.readouterr()
    assert captured.out == "function_error error: Test error Inputs: (), {}\n"
