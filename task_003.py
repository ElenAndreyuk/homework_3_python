# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list_1 = [1.3, 1, 3.5, 5.1, 10.02]
max_part = list_1[0] % 1
min_part = list_1[0] % 1

for i in list_1:
    if i % 1 > max_part:
        max_part = i % 1 
    elif i % 1 == 0:
        continue  
    elif i % 1 < min_part:
        min_part = i % 1  
    
    
print(round(max_part - min_part, 2))