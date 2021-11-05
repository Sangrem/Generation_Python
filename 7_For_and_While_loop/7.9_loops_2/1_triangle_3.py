res =0
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(res+1, end=' ')
        res+=1
    print()
