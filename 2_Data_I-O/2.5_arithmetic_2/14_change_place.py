#abc,acb,bac,bca,cab,cba.
num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10
print(a, b, c, '\n', a, c, b, '\n', b, a, c, '\n', b, c, a, '\n', c, a, b, '\n', c, b, a, sep="")
