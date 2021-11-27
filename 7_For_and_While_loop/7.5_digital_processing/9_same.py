n = int(input())

d = n % 10
res = "YES"

while n != 0:
    if d != n % 10:
        res = "NO"
    n //= 10
print(res)
