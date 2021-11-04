n = int(input())
if(n % 2 == 0):
    if(2 <= n <= 5):
        print("NO")
    elif(6 <= n <= 20):
        print("YES")
    elif(n > 20):
        print("NO")
elif n % 2 != 0:
    print("YES")
