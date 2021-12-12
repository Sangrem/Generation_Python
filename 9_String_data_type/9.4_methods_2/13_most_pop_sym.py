s = input()
a, b = 0, 0

for i in (s):
    if s.count(i) >= a:
        a = s.count(i)
        b = i

print(b)
