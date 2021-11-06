s, count = input(), 0
for i in range(1, len(s)):
    count += s[i] == s[i-1]
print(count)
