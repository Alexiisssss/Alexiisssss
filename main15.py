# Задача 15. Шестнадцатеричные и десятичные числа
# Условие.
# Напишите две функции с именами hex2int и int2hex для конвертации значений из шестнадцатеричной системы счисления
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно.
# Функция hex2int должна принимать на вход строку с единственным символом в шестнадцатеричной системе и преобразовывать его в число от нуля до 15 в десятичной системе,
# тогда как функция int2hex будет выполнять обратное действие – принимать десятичное число из диапазона от 0 до 15 и возвращать шестнадцатеричный эквивалент.
# Обе функции должны принимать единственный параметр со входным значением и возвращать преобразованное число.
# Удостоверьтесь, что функция hex2int корректно обрабатывает буквы в верхнем и нижнем регистрах.
# Если введенное пользователем значение выходит за допустимые границы, вы должны вывести сообщение об ошибке.


# Решение
def hex2int(hex_value):
    try:
        decimal_value = int(hex_value, 16)
        if 0 <= decimal_value <= 15:
            return decimal_value
        else:
            return 'Значение должно быть от 0 до F'
    except ValueError:
        return 'Некорректное значение шестнадцатеричной цифры'


def int2hex(decimal_value):
    if 0 <= decimal_value <= 15:
        hex_value = hex(decimal_value)[2:].upper()
        return hex_value
    else:
        return "Ошибка! Введенное значение должно быть от 0 до 15"


# Пример использования
if __name__ == "__main__":
    hex_digit = 'B'
    decimal_digit = 15

    print(f"Шестнадцатеричное '{hex_digit}' -> Десятичное {hex2int(hex_digit)}")
    print(f"Десятичное {decimal_digit} -> Шестнадцатеричное '{int2hex(decimal_digit)}'")
