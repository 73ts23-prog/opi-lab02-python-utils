"""Калькулятор із базовою перевіркою аргументів."""

from math import isfinite


def calculate(first, operation, second):
    """Виконує одну з операцій +, -, *, / над двома скінченними числами."""
    try:
        first, second = float(first), float(second)
    except (TypeError, ValueError) as error:
        raise ValueError('Потрібно ввести числа.') from error
    if not isfinite(first) or not isfinite(second):
        raise ValueError('Числа мають бути скінченними.')
    if operation == '+':
        result = first + second
    elif operation == '-':
        result = first - second
    elif operation == '*':
        result = first * second
    elif operation == '/':
        if second == 0:
            raise ValueError('Ділити на нуль не можна.')
        result = first / second
    else:
        raise ValueError('Невідома операція.')
    if not isfinite(result):
        raise ValueError('Результат виходить за межі скінченного числа.')
    return result
