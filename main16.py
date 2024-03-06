# Задача 3. Беспилотный автомобиль
# Условие. Это творческая задача.
# Представьте, что вы проектируете беспилотный автомобиль.
# Вам необходимо продумать, какими свойствами он обладает и какие действия совершает.
# Создайте класс беспилотный автомобиль и сохраните его в виде программного модуля.
# Импортируете класс и инициализируйте новый объект.


# Решение
class AutonomousCar:
    def __init__(self, model, speed=0, position=(0, 0)):
        self.model = model
        self.speed = speed
        self.position = position

    def move(self, direction):
        if direction == 'вперед':
            self.position = (self.position[0] + self.speed, self.position[1])
        elif direction == 'назад':
            self.position = (self.position[0] - self.speed, self.position[1])
        elif direction == 'влево':
            self.position = (self.position[0], self.position[1] - self.speed)
        elif direction == 'вправо':
            self.position = (self.position[0], self.position[1] + self.speed)

    def brake(self):
        self.speed = 0


# Пример использования
if __name__ == "__main__":
    car = AutonomousCar("Tesla Model S")
    print(f"Модель: {car.model}, Скорость: {car.speed}, Положение: {car.position}")

    car.speed = 50
    car.move('вперед')
    print(f"Модель: {car.model}, Скорость: {car.speed}, Положение: {car.position}")

    car.brake()
    print(f"Модель: {car.model}, Скорость: {car.speed}, Положение: {car.position}")
