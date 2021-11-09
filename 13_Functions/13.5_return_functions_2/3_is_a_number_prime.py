def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        if num != 1:
            return True
        else:
            return False

n = int(input())

print(is_prime(n))
