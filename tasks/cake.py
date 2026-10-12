def print_pack_report(number):
    for i in range(number, 0, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, '- расфасуем по 3 или по 5')
        elif i % 5 == 0:
            print(i, '- расфасуем по 5')
        elif i % 3 == 0:
            print(i, '- расфасуем по 3')
        else:
            print(i, '- не заказываем!')

print_pack_report(10)