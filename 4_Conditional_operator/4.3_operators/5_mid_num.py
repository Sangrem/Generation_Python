a, b, c = int(input()), int(input()), int(input())

if (a < b and b < c) or (c < b and b < a):
    print(b)
elif (b < a and a < c) or (c < a and a < b):
    print(a)
else:
    print(c)
