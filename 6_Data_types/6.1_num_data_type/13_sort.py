n1, n2, n3 = int(input()), int(input()), int(input())

nma = max(n1, n2, n3)
nmi = min(n1, n2, n3)

print(nma)
print((n1 + n2 + n3) - nma - nmi)
print(nmi)
