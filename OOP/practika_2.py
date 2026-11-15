class Transport:
    """Представляет транспортное средство."""

    def __init__(self, name):
        """Инициализирует транспортное средство.

        Args:
            name: Название транспортного средства.
        """
        self.name = name

    def description(self):
        """Возвращает описание транспортного средства."""
        return f"Транспорт - {self.name}"

class Car(Transport):
    """Представляет автомобиль."""

    def __init__(self, name, max_speed):
        """Инициализирует автомобиль.

        Args:
            name: Название автомобиля.
            max_speed: Максимальная скорость в км/ч.
        """
        super().__init__(name)
        self.max_speed = max_speed

    def description(self):
        """Возвращает описание автомобиля."""
        return f"Автомобиль - {self.name}, Макс. скорость - {self.max_speed} км/ч"

class Plane(Transport):
    """Представляет самолёт."""

    def __init__(self, name, altitude):
        """Инициализирует самолёт.

        Args:
            name: Название самолёта.
            altitude: Высота полёта в метрах.
        """
        super().__init__(name)
        self.altitude = altitude

    def description(self):
        """Возвращает описание самолёта."""
        return f"Самолёт - {self.name}, Высота полёта - {self.altitude} м"

class Bike(Transport):
    """Представляет велосипед."""

    def __init__(self, name, type_bike):
        """Инициализирует велосипед.

        Args:
            name: Название велосипеда.
            type_bike: Тип велосипеда.
        """
        super().__init__(name)
        self.type_bike = type_bike

    def description(self):
        """Возвращает описание велосипеда."""
        return f"Велосипед - {self.name}, Тип - {self.type_bike}"

car = Car("Тесла", 250)
plane = Plane("Боинг 737", 10_000)
bike = Bike("Кама", "Горный")

print(car.description())
print(plane.description())
print(bike.description())
