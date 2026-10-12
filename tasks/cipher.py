russian = 'абвгдеёжзийклмнпростуфхцчшщъыьэюя'
english = 'abcdefghijklmnopqrstuvwxyz'
def caesar_cipher(text):
    result = ''
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
    result = ''
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

text = input('Введите текст: ')
encrypted = caesar_cipher(text)
print('Зашифрованный текст:', encrypted)
print('Расшифрованный текст:', caesar_decipher(encrypted))




