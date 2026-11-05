import unittest

from python_utils.calculator import calculate
from python_utils.converter import convert_length


class CalculatorTests(unittest.TestCase):
    """Перевірки арифметичних операцій."""

    def test_operations(self):
        """Усі чотири операції мають наперед відомі результати."""
        for operation, expected in [('+', 10), ('-', 6), ('*', 16), ('/', 4)]:
            with self.subTest(operation=operation):
                self.assertEqual(calculate(8, operation, 2), expected)

    def test_zero_division(self):
        """Ділення на нуль має зрозумілу помилку."""
        with self.assertRaisesRegex(ValueError, 'нуль'):
            calculate(5, '/', 0)

    def test_unknown_operation(self):
        """Невідома операція відхиляється."""
        with self.assertRaises(ValueError):
            calculate(5, '?', 2)

    def test_invalid_numbers(self):
        """Нескінченні та нечислові значення відхиляються."""
        for number in ['abc', float('nan'), float('inf')]:
            with self.subTest(number=number), self.assertRaises(ValueError):
                calculate(number, '+', 2)


class ConverterTests(unittest.TestCase):
    """Перевірки перетворення одиниць довжини."""

    def test_supported_conversions(self):
        """Перетворення між усіма підтриманими одиницями."""
        cases = [(1, 'km', 'm', 1000), (250, 'cm', 'm', 2.5),
                 (1250, 'm', 'km', 1.25), (1.5, 'm', 'cm', 150),
                 (2, 'km', 'cm', 200000), (200000, 'cm', 'km', 2)]
        for value, source, target, expected in cases:
            with self.subTest(source=source, target=target):
                self.assertAlmostEqual(convert_length(value, source, target), expected)

    def test_zero_and_same_unit(self):
        """Нульова довжина та незмінна одиниця обробляються правильно."""
        self.assertEqual(convert_length(0, 'm', 'km'), 0)
        self.assertEqual(convert_length(12, 'm', 'm'), 12)

    def test_invalid_value(self):
        """Від'ємні, нескінченні й текстові значення відхиляються."""
        for value in [-1, 'abc', float('inf'), float('nan')]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                convert_length(value, 'm', 'km')

    def test_unknown_unit(self):
        """Невідома вихідна або кінцева одиниця відхиляється."""
        for source, target in [('inch', 'm'), ('m', 'inch')]:
            with self.subTest(source=source, target=target), self.assertRaises(ValueError):
                convert_length(1, source, target)


if __name__ == '__main__':
    unittest.main()
