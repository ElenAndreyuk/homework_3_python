# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('введите число: '))  
list_f =[]
def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n-1)+ fib(n-2)    

def fib_neg(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1    
    else:
        return fib(n-1)+ fib(n-2)    

for e in range(1, n +1):
    list_f.append(fib(e))
n = -n
list_f.insert(0, 0)
# list_f.insert(0, 1)
# list_f.insert(0, -1)
for i in range(-1, n, -1):
    list_f.insert(0, fib_neg(i))
print(list_f)


