n, count = str(input()), 0

while n != "стоп" and n != "хватит" and n != "достаточно":
    count += 1
    n = str(input())
print(count)
