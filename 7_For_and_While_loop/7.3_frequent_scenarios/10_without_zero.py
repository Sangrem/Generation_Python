res = 1

for i in range(10):
    n = int(input())
    res *= n + (n == 0)
print(res)
