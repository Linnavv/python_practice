class Employee:
    """Представляет сотрудника компании."""

    def __init__(self, id, name, base_money):
        """Инициализирует данные сотрудника.

        Args:
            id: Идентификатор сотрудника.
            name: Имя сотрудника.
            base_money: Базовая зарплата.
        """
        self.id = id
        self.name = name
        self.base_money = base_money

    def calculate_salary(self):
        """Возвращает базовую зарплату сотрудника."""
        return self.base_money

class Manager(Employee):
    """Представляет менеджера компании."""

    def __init__(self, id, name, base_money, bonus):
        """Инициализирует данные менеджера.

        Args:
            id: Идентификатор менеджера.
            name: Имя менеджера.
            base_money: Базовая зарплата.
            bonus: Премия менеджера.
        """
        super().__init__(id, name, base_money)
        self.bonus = bonus

    def calculate_salary(self):
        """Возвращает зарплату менеджера с учетом премии."""
        return self.base_money + self.bonus

class Developer(Employee):
    """Представляет разработчика компании."""

    def __init__(self, id, name, base_money, project_sum):
        """Инициализирует данные разработчика.

        Args:
            id: Идентификатор разработчика.
            name: Имя разработчика.
            base_money: Базовая зарплата.
            project_sum: Количество проектов.
        """
        super().__init__(id, name, base_money)
        self.project_sum = project_sum

    def calculate_salary(self):
        """Возвращает зарплату разработчика с учетом проектов."""
        return self.base_money + self.project_sum * 10_000

emp_alex = Employee(0, "Alex", 50_000)
manager_ivan = Manager(1, "Ivan", 50_000, 10_000)
dev_eva = Developer(2, "Eva", 50_000, 5)

print(emp_alex.calculate_salary())
print(manager_ivan.calculate_salary())
print(dev_eva.calculate_salary())
