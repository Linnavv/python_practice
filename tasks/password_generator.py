import random

print('=' * 35)
print('      ГЕНЕРАТОР ПАРОЛЕЙ')
print('=' * 35)

length = int(input('Введите длину пароля: '))

lower = input('Строчные буквы? (да/нет): ').lower()
upper = input('Заглавные буквы? (да/нет): ').lower()
digits = input('Цифры? (да/нет): ').lower()
special = input('Спецсимволы? (да/нет): ').lower()

characters = ''

if lower == 'да':
    characters += 'abcdefghijklmnopqrstuvwxyz'

if upper == 'да':
    characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if digits == 'да':
    characters += '0123456789'

if special == 'да':
    characters += '!@#$%&*?'

if characters == '':
    print('Вы не выбрали ни одного типа символов!')
elif length <= 0:
    print('Длина пароля должна быть больше нуля!')
else:
    password = ''

    for i in range(length):
        password += random.choice(characters)

    print('=' * 35)
    print('Ваш пароль:', password)
    print('=' * 35)