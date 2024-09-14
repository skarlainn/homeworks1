def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску."""
    card_number = str(card_number)
    if len(str(card_number)) == 16:
        return f"{card_number[0:3]} {card_number[4:6]}** **** {card_number[12:16]}"
    else:
        return "Ошибка ввода"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску."""
    if len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Ошибка ввода"