from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def logging(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} - ok\n")
                else:
                    print(f"{func.__name__} - ok")
            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error} Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error} Inputs: {args}, {kwargs}")
                raise

            return result

        return wrapper

    return logging

# Пример использования декоратора:
@log(filename="mylog.txt")
def func(x, y):
    return x + y
func(1, 2)