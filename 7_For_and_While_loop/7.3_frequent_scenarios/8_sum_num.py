n = int(input())
counter = 0
for i in range(1, n + 1):
    if ((i ** 2) % 10 == 5):
        counter += i
print(counter)
