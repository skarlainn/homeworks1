from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src.read_from_file import read_from_csv, read_from_excel


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file: MagicMock) -> None:
    result = read_from_csv("..\\data\\transactions.csv")
    assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file: MagicMock) -> None:
    result = read_from_csv("..\\data\\transactions.csv")
    assert result == []



@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found_excel(mock_file: MagicMock) -> None:
    result = read_from_excel("..\\data\\transactions_excel.xlsx")
    assert result == []


@patch("src.read_from_file.pd.read_excel")
def test_empty_excel_file(mock_file: MagicMock) -> None:
    mock_file.side_effect = pd.errors.EmptyDataError()
    result = read_from_excel("..\\data\\transactions_excel.xlsx")
    assert result == []