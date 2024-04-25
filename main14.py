# Задача 14. Случайный номерной знак
# Условие.
# Представьте, что в вашем регионе устаревшим является формат номерных автомобильных знаков из трех букв, следом за которыми идут три цифры.
# Когда все номера такого шаблона закончились, было решено обновить формат, поставив в начало четыре цифры, а за ними три буквы.
# Напишите функцию, которая будет генерировать случайный номерной знак.
# При этом номера в старом и новом форматах должны создаваться примерно с одинаковой вероятностью.
# В основной программе нужно сгенерировать и вывести на экран случайный номерной знак.


# Решение
import random


def generate_numbers():
    letters = ['A', 'Б', 'E', 'K', 'M', 'Н', 'O', 'C', 'T', 'Y', 'X']
    old_format = random.randint(0, len(letters) ** 3 - 1)  # 1728 символов для трехбуквенного номера
    new_format = random.randint(0, 9999)  # максимальноe кол-во символов для четырех цифр

    if random.random() < 0.5:
        return f"Старый формат: {letters[old_format // len(letters) ** 2]}{letters[(old_format // len(letters)) % len(letters)]}{letters[old_format % len(letters)]}-{new_format:04}"
    else:
        return f"Новый формат: {new_format:04}-{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}"


print(generate_numbers())

