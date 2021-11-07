c = input().lower().split()
count = 0
count = c.count('an') + c.count('a') + c.count('the')
print("Общее количество артиклей:", count)
