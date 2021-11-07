n = int(input())
l1 = []
l2 = []
for _ in range(n):
    x = int(input())
    l1.append(x)
for i in range(len(l1) - 1):
    l2.append(l1[i] + l1[i+1])
print(l2)
