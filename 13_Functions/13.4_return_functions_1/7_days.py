def get_days(month):
    m = [31,28,31,30,31,30,31,31,30,31,30,31]
    return m[num - 1]

num = int(input())
 
print(get_days(num))
