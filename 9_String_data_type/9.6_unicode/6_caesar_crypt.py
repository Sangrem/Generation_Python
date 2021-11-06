n = int(input())
for i in input():
    print(chr(((ord(i) - ord("a") - n) % 26) + ord("a")), end="")
