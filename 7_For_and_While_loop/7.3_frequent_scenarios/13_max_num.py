c = int(input())
m1, m2 = 0, 0
for i in range(c):
    if n > m1:
        m2 = m1
        m1 = n
    elif n < m1 and n > m2:
        m2 = n
print(m1)
print(m2)
