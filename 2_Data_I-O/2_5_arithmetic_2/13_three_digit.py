num = int(input())
n1 = num // 100
n2 = (num % 100) // 10
n3 = num % 10
print("Сумма цифр =", n1 + n2 + n3)
print("Произведение цифр =", n1 * n2 * n3)
