from math import pi, tan

n, a = float(input()), float(input())
res = (n * a ** 2) / (4 * tan(pi / n))
print(res)
