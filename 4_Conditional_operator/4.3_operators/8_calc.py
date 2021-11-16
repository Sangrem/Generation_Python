a, b, s = int(input()), int(input()), input()

if s == "*":
    print(a * b)
elif s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "/":
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя!")
else:
    print("Неверная операция")
