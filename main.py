"""Демонстрація модулів навчального проєкту."""

from python_utils.calculator import calculate
from python_utils.converter import convert_length


def main():
    """Показує результати обчислень і обробку помилки."""
    print('Python Utilities | Цвіркунов Олексій Дмитрович | ІПЗ-21')
    print(f"8 + 2 = {calculate(8, '+', 2):g}")
    print(f"8 / 2 = {calculate(8, '/', 2):g}")
    print(f"1.5 km = {convert_length(1.5, 'km', 'm'):g} m")
    print(f"250 cm = {convert_length(250, 'cm', 'm'):g} m")
    try:
        calculate(5, '/', 0)
    except ValueError as error:
        print(f'Перевірка помилки: {error}')


if __name__ == '__main__':
    main()
