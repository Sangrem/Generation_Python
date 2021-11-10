def is_magic(date):
    day, month, year = date.split('.')
    return int(day) * int(month) == int(year) % 100

date = input()

print(is_magic(date))
