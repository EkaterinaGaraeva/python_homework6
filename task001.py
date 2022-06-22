# 1 - Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. 
# Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

def list_of_numbers_and_operations(new_string):
    list_of_numbers = []
    num = ''
    for i in range(len(new_string)):
        if new_string[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            num += new_string[i]
            if i == len(new_string) - 1:
                list_of_numbers.append(num)
        elif new_string[i] in ['*', '/', '+', '-']:
            if new_string[i-1] not in [')']:
                list_of_numbers.append(num)
            list_of_numbers.append(new_string[i])
            num =''
        elif new_string[i] in ['(']:
            list_of_numbers.append(new_string[i])
            num =''
        elif new_string[i] in [')']:
            list_of_numbers.append(num)
            list_of_numbers.append(new_string[i])
    return list_of_numbers

def calculation(list_of_numbers):
    while '/' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "/":
                result = float(list_of_numbers[i-1]) / float(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    while '*' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "*":
                result = float(list_of_numbers[i-1]) * float(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    while '-' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "-":
                result = float(list_of_numbers[i-1]) - float(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    while '+' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "+":
                result = float(list_of_numbers[i-1]) + float(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    result = list_of_numbers[0]
    return result

def parentheses(list_of_numbers):
    while '(' in list_of_numbers or ')' in list_of_numbers:
        begin = 0
        end = len(list_of_numbers)
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == '(':
                begin = i + 1
                # print(begin)
            if list_of_numbers[i] == ')':
                end = i
                # print(end)
                list_in_parenthese = []
                for j in range(begin, end):
                    list_in_parenthese.append(list_of_numbers[j])
                # print(list_in_parenthese)
                result = calculation(list_in_parenthese)
                # print(result)
                list_of_numbers[begin - 1] = result
                del list_of_numbers[begin: end + 1]
                # print(list_of_numbers)
                break
    result = calculation(list_of_numbers)
    return result

str_one = '2+2'
str_two = '1+2*3'
str_three = '1-2*3'
str_four = '(1+2)*3'
numbers_one = list_of_numbers_and_operations(str_one)
numbers_two = list_of_numbers_and_operations(str_two)
numbers_three = list_of_numbers_and_operations(str_three)
numbers_four = list_of_numbers_and_operations(str_four)
# print(numbers_one)
# print(numbers_two)
# print(numbers_three)
# print(numbers_four)
print(f'{str_one} => {parentheses(numbers_one)}')
print(f'{str_two} => {parentheses(numbers_two)}')
print(f'{str_three} => {parentheses(numbers_three)}')
print(f'{str_four} => {parentheses(numbers_four)}')
