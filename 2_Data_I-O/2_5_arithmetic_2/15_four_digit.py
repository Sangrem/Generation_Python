num = int(input())
n1 = num // 1000
n2 = (num % 1000) // 100
n3 = (num % 100) // 10
n4 = num % 10
print("Цифра в позиции тысяч равна",n1)
print("Цифра в позиции сотен равна",n2)
print("Цифра в позиции десятков равна",n3)
print("Цифра в позиции единиц равна",n4)
