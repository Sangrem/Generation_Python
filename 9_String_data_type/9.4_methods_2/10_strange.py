n = int(input())
cout = 0

for i in range (n):
    s = input()
    if s.count("11") >= 3:
        cout += 1

print(cout)
