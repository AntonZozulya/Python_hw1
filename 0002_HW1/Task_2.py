
# Найдите сумму цифр трехзначного числа.

# Пример:

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# РЕШЕНИЕ:

n = int(input("Введите трехзначное число: "))
a = int(n // 100) 
b = int(n / 10 % 10)
c = int(n % 10)
result = a + b + c
print(result)