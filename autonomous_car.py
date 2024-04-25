class AutonomousCar:
    def __init__(self, model, speed=0, battery_level=100, max_distance=1000):
        self.model = model
        self.speed = speed
        self.battery_level = battery_level
        self.max_distance = max_distance

    def move(self, speed):
        self.speed = speed

    def charge_battery(self):
        self.battery_level = 100

    def __str__(self):
        return f"Model: {self.model}, Speed: {self.speed}, Battery Level: {self.battery_level}, Max Distance: {self.max_distance}"