import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("70007922896063611", "Ошибка ввода"),
    ("700079228960636", "Ошибка ввода"),
    ("70007922896063ab", "Ошибка ввода"),
    (" ", "Ошибка ввода")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("736541084301358743055", "Ошибка ввода"),
    ("7365410843013587430", "Ошибка ввода"),
    ("736541084301358743ab", "Ошибка ввода"),
    (" ", "Ошибка ввода")
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected