class Product:
    """Представляет товар в интернет-магазине."""

    def __init__(self, name, price, stock, category):
        """Инициализирует данные товара."""
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

class ShoppingCart:
    """Представляет корзину покупателя."""

    def __init__(self):
        """Создаёт пустую корзину."""
        self.items = {}

    def add_product(self, product, quantity):
        """Добавляет товар в корзину."""
        if quantity > 0 and quantity <= product.stock:
            current_quantity = self.items.get(product, 0)

            if current_quantity + quantity <= product.stock:
                self.items[product] = current_quantity + quantity

    def remove_product(self, product):
        """Удаляет товар из корзины."""
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        """Изменяет количество товара в корзине."""
        if product in self.items:
            if quantity > 0 and quantity <= product.stock:
                self.items[product] = quantity
            elif quantity <= 0:
                del self.items[product]

class Order:
    """Представляет заказ покупателя."""

    def __init__(self, items, discount=0.1, tax=0.2):
        """Инициализирует заказ."""
        self.items = items.copy()
        self.discount = discount
        self.tax = tax
        self.total = 0

    def calculate_total(self):
        """Рассчитывает стоимость заказа со скидкой и налогом."""
        total = 0

        for product, quantity in self.items.items():
            total += product.price * quantity

        total = total - total * self.discount
        total = total + total * self.tax

        self.total = total
        return self.total

    def process_order(self):
        """Оформляет заказ и обновляет остатки товаров."""
        for product, quantity in self.items.items():
            if quantity > product.stock:
                return "Недостаточно товара на складе"

        for product, quantity in self.items.items():
            product.stock -= quantity

        return self.calculate_total()

class Customer:
    """Представляет покупателя интернет-магазина."""

    def __init__(self, name, email):
        """Инициализирует данные покупателя."""
        self.name = name
        self.email = email
        self.order_history = []

    def place_order(self, cart):
        """Оформляет заказ и сохраняет его в истории."""
        order = Order(cart.items)
        result = order.process_order()

        if isinstance(result, (int, float)):
            self.order_history.append(order)
            cart.items.clear()

        return result

laptop = Product("Ноутбук", 80_000, 5, "Электроника")
mouse = Product("Мышь", 2_000, 10, "Аксессуары")

customer = Customer("Алексей", "alex@example.com")
cart = ShoppingCart()

cart.add_product(laptop, 1)
cart.add_product(mouse, 2)
cart.update_quantity(mouse, 3)

order = customer.place_order(cart)

print(f"Покупатель: {customer.name}")
print(f"Стоимость заказа: {order:.2f}")
print(f"Заказов в истории: {len(customer.order_history)}")
print(f"Ноутбуков осталось: {laptop.stock}")
print(f"Мышей осталось: {mouse.stock}")
