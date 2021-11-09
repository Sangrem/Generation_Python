def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep="")

name, surname, patronymic = input().capitalize(), input().capitalize(), input().capitalize()

print_fio(name, surname, patronymic)
