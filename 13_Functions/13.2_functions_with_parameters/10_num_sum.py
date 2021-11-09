def print_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num%10
        num //= 10
    print(sum)

n = int(input())
 
print_digit_sum(n)
