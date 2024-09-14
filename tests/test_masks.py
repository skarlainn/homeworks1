import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ('7000792289606361', '7000 79** **** 6361'),
    ('70007922896063611', "Ошибка ввода"),
    ('700079228960636', "Ошибка ввода"),
    ('70007922896063ab', "Ошибка ввода")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected