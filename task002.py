# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок 
# из какой-то книги, а втором файлике — сжатая версия этого текста).

import codecs

with codecs.open('RLE_decoded.txt', encoding='utf-8') as data:
    my_text = data.read()
    # print(my_text)
    # print('\n')

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

str_code = encode_rle(my_text)
print(f'\nСжатая версия текста: \n{str_code}')

with codecs.open('RLE_encoded.txt', 'w', "utf-8") as data:
    data.write(str_code)

with codecs.open('RLE_encoded.txt', encoding='utf-8') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print(f'\nОтрывок из книги: \n{str_decode}')
