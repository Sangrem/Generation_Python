n = int(input())
l = []
temp = 0
while n != 0:
    temp = int(input())
    l.append(temp)
    n -= 1
del l[1::2]
print(l)
