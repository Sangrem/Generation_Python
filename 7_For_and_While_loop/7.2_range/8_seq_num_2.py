m, n = int(input()), int(input())

if m == n:
    print(m)
elif m < n:
    for i in range(m, n+1):
        print(i)
elif m > n:
    for j in range(m, n-1, -1):
        print(j)
