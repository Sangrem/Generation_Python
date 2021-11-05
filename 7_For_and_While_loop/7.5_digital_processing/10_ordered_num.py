n, res = int(input()), "YES"
while n // 10 != 0:
    x = n % 10
    n //= 10
    if x > n % 10:
        res = "NO"
print(res)
