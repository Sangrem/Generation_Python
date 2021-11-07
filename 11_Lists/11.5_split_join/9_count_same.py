L = map(int, input().split())
obj =  {}
for k in L:
    obj[k] = obj.get(k, 0) + 1
count = 0
for n in obj.values():
    count += (n - 1) * n / 2
print(int(count))
