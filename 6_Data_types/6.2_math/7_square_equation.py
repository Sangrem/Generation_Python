a, b, c = float(input()), float(input()), float(input())
res = b ** 2 - 4 * a * c
if res < 0:
    print("Нет корней")
elif res == 0:
    print(-b / (2 * a))
elif res > 0:
    x1 = (-b - res ** 0.5) / (2*a)
    x2 = (-b + res ** 0.5) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))
