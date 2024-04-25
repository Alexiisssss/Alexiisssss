# Продолжение задачи 17.
# Задача:
# Брать ли студенту курс дополнительной подготовки перед сдачей экзамена.
# Для этой задачи мы можем использовать класс Neuron.
# Входные параметры, влияющие на принятие решения:
#
#
# Оценка(кол-во баллов) за последний тест (от 0 до 100).
# Количество часов, потраченных на подготовку за неделю.
# Уровень самоуверенности (от 0 до 10).
# Оценка(балл) за предыдущий экзамен (от 0 до 100).


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def weighted_sum(self, inputs):
        if len(inputs) != len(self.weights):
            return "Number of input must match numbers of weights"
        weighted_sum = self.bias
        for i in range(len(inputs)):
            weighted_sum += inputs[i] * self.weights[i]
        return weighted_sum

    def step_function(self, weighted_sum):
        return 1 if weighted_sum >= 0 else 0


weights = [0.4, 0.3, 0.2, 0.1]
bias = -0.5
neiron = Neuron(weights, bias)

test_score = 75
study_hours_per_week = 8
confidence_level = 7
previous_exam_score = 85

inputs = [test_score, study_hours_per_week, confidence_level, previous_exam_score]
weighted_sum = neiron.weighted_sum(inputs)

decision = neiron.step_function(weighted_sum)

if decision == 1:
    print("Рекомендуется брать курс дополнительной подготовки перед экзаменом.")
else:
    print("Не рекомендуется брать курс дополнительной подготовки перед экзаменом.")
