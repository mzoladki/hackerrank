import sys
a, b, c, d, e = input().strip().split(' ')

tab = [int(a), int(b), int(c), int(d), int(e)]

mini = sys.maxsize
maxi = 0

x = 0
tmp = 0

for i in range(len(tab)):
    for j in range(len(tab)):
        if x == j:
            pass
        else:
            tmp += tab[j]
    if tmp > maxi:
        maxi = tmp
    if tmp < mini:
        mini = tmp
    x += 1
    tmp = 0

print(mini, end=" ")
print(maxi, end=" ")
