from src.masks import get_mask_card_number


def mask_account_card(numbers: str) -> str:
    """Функция, которая маскирует номер карты и счета"""

    if "Счет" in numbers:
        mask_account = f"{numbers[:-20]}**{numbers[-4::]}"
        return mask_account
    else:
        card = get_mask_card_number(numbers[-16:])
        mask_card = numbers.replace(numbers[-16:], card)
        return mask_card

def get_date (date: str) -> str:
    """Функция, которая принимает на вход строку с датой"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"