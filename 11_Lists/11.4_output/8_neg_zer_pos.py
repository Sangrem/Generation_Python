n = int(input())
l = [int(input()) for _ in range(n)]
neg, zer, pos = [], [], []
for i in l:
    if i < 0:
        neg.append(i)
    elif i == 0:
        zer.append(i)
    else:
        pos.append(i)
L = neg + zer + pos
for j in L:
    print(j, end="\n")
