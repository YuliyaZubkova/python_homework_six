from functools import lru_cache
import sys

sys.setrecursionlimit(5000)

@lru_cache()
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("Введите количество чисел фибоначчи: "))
list_1 = []
for i in range(1, n+1):
    list_1.append(fib(i))
print(f"Последовательность фибоначчи: {list_1}")
print(f"Максимальный элемент: {max(list_1)}")
#print(f"Минимальный элемент: {min(list_1)}")




