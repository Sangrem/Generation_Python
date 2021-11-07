n = int(input())
s = [input() for _ in range(n)]
z = input()
for i in range(len(s)):
    if z.lower() in s[i].lower():
        print(s[i],sep="\n")
