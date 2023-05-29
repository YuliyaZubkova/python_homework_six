'''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)

min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))
lst = [2, 5, 10, 8, 3, 6, 1, 7, 4]
indexes = []
for i in range(len(lst)):
    if min_value <= lst[i] <= max_value:
        indexes.append(i)
print(indexes)

Эталонное решение:
'''
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)

