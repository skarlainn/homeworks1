import logging
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    card_number = str(card_number)
    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Маскировка номера карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        logger.warning(f"Неверный номер карты: длина номера - {len(card_number)}")
        return None


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    account_number = str(account_number)
    if account_number.isdigit() and len(account_number) == 20:
        logger.info("Маскировка номера счета")
        return f"**{account_number[-4:]}"
    else:
        logger.warning(f"Неверный номер счета: длина номера - {len(account_number)}")
        return None
