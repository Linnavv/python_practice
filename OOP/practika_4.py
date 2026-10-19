class SpaceShip:
    """Представляет космический корабль."""

    def __init__(self, fuel, hull_condition, speed):
        """Инициализирует параметры корабля."""
        self.fuel = fuel
        self.hull_condition = hull_condition
        self.speed = speed

    def change_speed(self, speed):
        """Изменяет скорость корабля."""
        self.speed = speed

    def use_fuel(self, amount):
        """Уменьшает запас топлива."""
        if amount > 0 and amount <= self.fuel:
            self.fuel -= amount

    def damage_hull(self, damage):
        """Уменьшает состояние корпуса."""
        if damage > 0:
            self.hull_condition -= damage

            if self.hull_condition < 0:
                self.hull_condition = 0

class CrewMember:
    """Представляет члена экипажа."""

    def __init__(self, name, role, health, skill):
        """Инициализирует данные члена экипажа."""
        self.name = name
        self.role = role
        self.health = health
        self.skill = skill

    def take_damage(self, damage):
        """Уменьшает здоровье члена экипажа."""
        if damage > 0:
            self.health -= damage

            if self.health < 0:
                self.health = 0

    def show_info(self):
        """Возвращает информацию о члене экипажа."""
        return (
            f"Имя: {self.name}, Роль: {self.role}, "
            f"Здоровье: {self.health}, Навык: {self.skill}"
        )

class Mission:
    """Представляет космическую миссию."""

    def __init__(self, goal, resources):
        """Инициализирует цель и ресурсы миссии."""
        self.goal = goal
        self.resources = resources
        self.events = []

    def add_event(self, event):
        """Добавляет событие в миссию."""
        self.events.append(event)

    def use_resources(self, amount):
        """Уменьшает количество ресурсов миссии."""
        if amount > 0 and amount <= self.resources:
            self.resources -= amount

    def show_info(self):
        """Выводит информацию о миссии."""
        print(f"Цель миссии: {self.goal}")
        print(f"Остаток ресурсов: {self.resources}")
        print(f"События миссии: {self.events}")

ship = SpaceShip(100, 100, 0)

pilot = CrewMember("Алекс", "Пилот", 100, "Управление кораблём")
engineer = CrewMember("Ева", "Инженер", 100, "Ремонт корабля")

mission = Mission("Исследование Марса", 200)

ship.change_speed(500)
ship.use_fuel(20)

ship.damage_hull(15)
engineer.take_damage(10)

mission.use_resources(50)
mission.add_event("Встреча с астероидом")
mission.add_event("Успешное прохождение опасного участка")

print(f"Топливо: {ship.fuel}")
print(f"Состояние корпуса: {ship.hull_condition}%")
print(f"Скорость корабля: {ship.speed} км/ч")

print(pilot.show_info())
print(engineer.show_info())

mission.show_info()
