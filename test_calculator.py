import calculator

def test_add():
    """Проверяет сложение двух чисел."""
    assert calculator.add(2, 3) == 5

test_add()
print("Тест пройден!")