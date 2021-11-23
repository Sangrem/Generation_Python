m, n = int(input()), int(input())

r = ((m - 1) // 2) * 2 + 1

for i in range(r, n - 1, - 2):
    print(i)
