n = int(input())
s = [input() for _ in range(n)]
l = []
for i in range(len(s)):
    l.extend(s[i])
print(l)
