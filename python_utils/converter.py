"""Перетворення одиниць довжини."""

from math import isfinite


def convert_length(value, source, target):
    """Перетворює невід'ємну довжину між m, km і cm."""
    factors = {'m': 1, 'km': 1000, 'cm': 0.01}
    if source not in factors or target not in factors:
        raise ValueError('Підтримуються одиниці m, km і cm.')
    try:
        value = float(value)
    except (TypeError, ValueError) as error:
        raise ValueError('Довжина має бути числом.') from error
    if not isfinite(value) or value < 0:
        raise ValueError('Довжина має бути невід’ємним скінченним числом.')
    result = value * factors[source] / factors[target]
    if not isfinite(result):
        raise ValueError('Результат виходить за межі скінченного числа.')
    return result
