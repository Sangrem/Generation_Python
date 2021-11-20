from math import sqrt

a, b = float(input()), float(input())

r1 = (a + b) / 2
r2 = sqrt(a * b)
r3 = (2 * a * b) / (a + b)
r4 = sqrt((a ** 2 + b ** 2) / 2)

print(r1)
print(r2)
print(r3)
print(r4)
