a, b = input(), input()
if a == b and (a == 'красный' or a == 'желтый' or a == 'синий'):
    print(a)
elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
    print('оранжевый')
elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
    print('зеленый')
else:
    print('ошибка цвета')
