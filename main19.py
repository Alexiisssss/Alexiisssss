# Задача 19. Книги без буквы E.
# Условие.
# В истории литературы известен случай написания романа объемом около 50 тыс. слов,
# в котором ни разу не была употреблена самая популярная в английском алфавите буква E.
# Название его – «Gadsby». Напишите программу, которая будет считывать список слов из файла и собирать статистику о том,
# в каком проценте слов используется каждая буква алфавита.
# Выведите результат для всех 26 букв английского алфавита и отдельно отметьте букву, которая встречалась в словах наиболее редко.
# В вашей программе должны игнорироваться знаки препинания и регистр символов.


# Решение

import string


def calculate_letter_percentage(word_list):
    letter_count = {letter: 0 for letter in string.ascii_lowercase}  # словарь
    total_letters = 0  # счетчик

    for word in word_list:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                letter_count[letter] += 1
                total_letters += 1

    letter_percentage = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}
    return letter_percentage


def least_used_letter(letter_percentage):
    min_percentage = min(letter_percentage.values())
    least_used_letters = [letter for letter, percentage in letter_percentage.items() if percentage == min_percentage]
    return least_used_letters


with open("input.txt", "r") as file:
    words = file.read().split()

letter_percentage = calculate_letter_percentage(words)

for letter, percentage in sorted(letter_percentage.items()):
    print(f"{letter}: {percentage:.2f}%")

least_used = least_used_letter(letter_percentage)
print(f"\nНаименее часто встречающаяся буква(ы): {' '.join(least_used)}")
