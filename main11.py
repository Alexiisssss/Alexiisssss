# Задача 11. Ниже и выше среднего.
# Условие.
# Напишите программу, которая будет запрашивать у пользователя числа, пока не будет введена пустая строка.
# Сначала на экран должно быть выведено среднее значение введенного ряда чисел,
# после этого друг за другом необходимо вывести список чисел ниже среднего, равных ему (если такие найдутся) и выше среднего.
# Каждый список должен предваряться соответствующим заголовком.


#Решение

numbers_list = []
total = 0

while True:
    numbers = input("Введите числа или оставьте поле пустым для выхода: ")
    if numbers == "":
        break
    num = float(numbers)
    numbers_list.append(num)
    total += num

avg = total / len(numbers_list) if numbers_list else 0

below = [num for num in numbers_list if num < avg]
equal = [num for num in numbers_list if num == avg]
above = [num for num in numbers_list if num > avg]

print(f"Среднее значение: {avg}")
print(f"Числа ниже среднего: ", below)
print(f"Числа равные среднему значению: ", equal)
print(f"Числа выше среднего значения: ", above)