n = int(input())
s = [input() for _ in range (n)]
k = int(input())
for i in range(n):
    l = []
    l.extend(s[i])
    if k <= len(l):
        print(l[k-1], end="")
    else:
        continue
