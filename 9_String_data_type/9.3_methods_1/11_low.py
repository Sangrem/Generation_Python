s = input()
count = 0
for i in range(len(s)):
    if s[i].islower():
        count += 1
print(count)
