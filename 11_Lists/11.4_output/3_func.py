n = int(input())
s = [input() for _ in range (n)]
s1 = []
print(*s, sep="\n")
print()
for i in range(len(s)):
    r = int(s[i]) ** 2 + 2 * int(s[i]) + 1
    s1.append(r)
print(*s1, sep="\n")
