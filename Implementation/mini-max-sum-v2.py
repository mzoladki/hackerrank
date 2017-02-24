import sys

a, b, c, d, e = input().strip().split(' ')

tab = [int(a), int(b), int(c), int(d), int(e)]

mini = sys.maxsize
maxi = 0

for i in tab:
    tmp = sum(tab)-i
    if tmp > maxi:
        maxi = tmp
    if tmp < mini:
        mini = tmp

print(mini,maxi)
