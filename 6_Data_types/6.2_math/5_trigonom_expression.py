from math import sin, cos, tan, radians

x = float(input())

x = radians(x)
res = sin(x) + cos(x) + tan(x) ** 2

print(res)
