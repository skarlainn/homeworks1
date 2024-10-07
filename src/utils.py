import json
feature/homework_12_2
import logging
import os
develop
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion

feature/homework_12_2
current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


develop

def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
 feature/homework_12_2
        logger.info("Открытие файла с транзакциями")

develop
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                return []
        if not isinstance(transactions, list):
feature/homework_12_2
            logger.error("Список транзакций пуст")
            return []
        logger.info("Создан список словарей с данными о финансовых транзакциях")
        return transactions
    except FileNotFoundError:
        logger.error("Файл не найден")

            return []
        return transactions
    except FileNotFoundError:
 develop
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
 feature/homework_12_2
        logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion(trans)
        logger.error("Код валюты транзакции не RUB, произведена конвертация")

    else:
        amount = currency_conversion(trans)
develop
    return amount
