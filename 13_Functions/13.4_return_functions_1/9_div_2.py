def number_of_factors(num):
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            l.append(i)
    return len(l)

n = int(input())
 
print(number_of_factors(n))
