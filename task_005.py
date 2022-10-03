# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('введите число: '))  
def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1)+ fib(n-2)    
def fib_neg(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return -1    
    else:
        return fib_neg(n-2) - fib_neg(n-1)   
list_f =[]
for i in range(2, n +1):
    list_f.insert(0, fib_neg(i))
for e in range(0, n +1):
    list_f.append(fib(e))
print(list_f)

