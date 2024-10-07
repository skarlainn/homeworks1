import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896063611", []),
        ("700079228960636", []),
        ("70007922896063ab", []),
        (" ", []),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("736541084301358743055", []),
        ("7365410843013587430", []),
        ("736541084301358743ab", []),
        (" ", []),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
