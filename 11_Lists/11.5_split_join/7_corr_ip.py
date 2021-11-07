s = input().split('.')
count = 0
for i in range(len(s)):
    if 0 <= int(s[i]) <= 255:
        count += 1
if count == 4:
    print("ДА")
else:
    print("НЕТ")
