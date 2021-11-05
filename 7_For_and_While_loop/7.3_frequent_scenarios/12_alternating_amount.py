n = int(input())
res = 0
for i in range(n):
    if i % 2 == 0:
        res += i + 1
    else:
        res -= i + 1
print(res)
