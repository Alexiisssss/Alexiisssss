# Задача 3. Игра Fizz-Buzz.
# Условие.
# Fizz-Buzz – это известная игра, помогающая детям освоить в игровой форме правила деления.
# Участники садятся в круг, чтобы игра теоретически могла продолжаться бесконечно.
# Первый игрок говорит «Один» и передает ход тому, кто слева.
# Каждый следующий игрок должен мысленно прибавить к предыдущему числу единицу и произнести либо его, либо одно из ключевых слов:
# Fizz, если число без остатка делится на три, или Buzz, если на пять. Если соблюдаются оба этих условия, он произносит Fizz-Buzz.
# Игрок, не сумевший сказать правильное слово, выбывает из игры. Последний оставшийся игрок признается победителем.
# Разработайте программу, реализующую алгоритм игры Fizz-Buzz применительно к первым 100 числам. Каждый следующий ответ должен отображаться на новой строке.


# Решение
def fizz_buzz_game(num_players):
    players = list(range(1, num_players + 1))
    current_number = 1

    while len(players) > 1:
        for player in players.copy():
            user_input = input(f"Игрок {player}, введите ответ для числа {'*' * len(str(current_number))}: ")

            if current_number % 3 == 0 and current_number % 5 == 0:
                correct_answer = "Fizz-Buzz"
            elif current_number % 3 == 0:
                correct_answer = "Fizz"
            elif current_number % 5 == 0:
                correct_answer = "Buzz"
            else:
                correct_answer = str(current_number)

            if user_input.lower() != correct_answer.lower():
                print(f"Неверно! Игрок {player} выбывает из игры.")
                players.remove(player)
                if len(players) == 1:
                    break
            else:
                print(f"Верно, Игрок {player} ждите следующей вашей очереди.")
                current_number += 1

    if len(players) == 1:
        print(f"Поздравляем, игрок {players[0]} - победитель! ")
    else:
        print("Игра Завершена. Всем спасибо, вы молодцы!")


try:
    num_players = int(input("Введите количество игроков: "))
    if num_players < 1:
        raise ValueError
    fizz_buzz_game(num_players)
except ValueError:
    print("Ошибка: Введите положительное целое число для количества игроков.")
