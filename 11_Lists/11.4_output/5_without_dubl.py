r = []
for i in range(int(input())):
        s = input().lower()
        if s not in r:
                r.append(s)
print(*r, sep='\n')
