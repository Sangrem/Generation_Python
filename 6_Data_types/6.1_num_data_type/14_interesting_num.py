n = int(input())

n1 = n // 100
n2 = n // 10 % 10
n3 = n % 10
nmax = max(n1, n2, n3)
nmin = min(n1, n2, n3)
nmid = (n1 + n2 + n3) - nmax - nmin
res = nmax - nmin

if res == nmid:
    print("Число интересное")
else:
    print("Число неинтересное")
