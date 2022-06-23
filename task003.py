# 3 - ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, 
# которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.

# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно 
# (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

def encode_rot13(text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rot13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    text_rot13 = ''
    for i in text:
        index = alphabet.find(i)
        text_rot13 += rot13[index]
    return text_rot13

def decode_rot13(text_rot13):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rot13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    decode_text = ''
    for i in text_rot13:
        index = rot13.find(i)
        decode_text += alphabet[index]
    return decode_text

original_str = 'opq'
print(f'Изначальная строка - {original_str}')
encode_str = encode_rot13(original_str)
print(f'Зашифрованная строка - {encode_str}')
decode_str = decode_rot13(encode_str)
print(f'Расшифрованная строка - {decode_str}')

