# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
n = int(input('введите число: '))
number = ''
while n != 0:
    number = str(n % 2) + number
    n =  n//2
print(number)    