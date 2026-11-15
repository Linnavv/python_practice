"""
Программа шифрует и расшифровывает текст
с помощью шифра Цезаря со сдвигом на 3 символа.
Поддерживает русский и английский алфавиты.
"""

russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
english = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(text):
    """
    Шифрует текст, сдвигая каждую букву
    на 3 позиции вперёд в алфавите.

    text — текст, который нужно зашифровать.
    Возвращает зашифрованный текст.
    """
    result = ""
    for i in text:
        is_upper = i.isupper()
        i = i.lower()
        if i in russian:
            index = (russian.index(i) + 3) % len(russian)
            letter = russian[index]
            if is_upper:
                letter = letter.upper()
            result += letter
        elif i in english:
            index = (english.index(i) + 3) % len(english)
            letter = english[index]
            if is_upper:
                letter = letter.upper()
            result += letter
        else:
            result += i
    return result

def caesar_decipher(text):
    """
    Расшифровывает текст, сдвигая каждую букву
    на 3 позиции назад в алфавите.

    text — зашифрованный текст.
    Возвращает расшифрованный текст.
    """
    result = ""
    for i in text:
        is_upper = i.isupper()
        i = i.lower()

        if i in russian:
            index = (russian.index(i) - 3) % len(russian)
            letter = russian[index]
            if is_upper:
                letter = letter.upper()
            result += letter

        elif i in english:
            index = (english.index(i) - 3) % len(english)
            letter = english[index]
            if is_upper:
                letter = letter.upper()
            result += letter

        else:
            result += i

    return result

text = input("Введите текст: ")
encrypted = caesar_cipher(text)
print("Зашифрованный текст:", encrypted)
print("Расшифрованный текст:", caesar_decipher(encrypted))


