#!/bin/python3

import sys

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

same_location = False

if ((x1 < x2) and (v1 < v2)) or ((x2 > x1) and (v2 > v1)):
    print("NO")
elif ((x1 < x2) and v1 == v2) or ((x2 < x1) and (v1 == v2)):
    print("NO")
else:
    if x1 < x2:
        while x1 < x2:
            x1 = x1+v1
            x2 = x2+v2
            if x1 == x2:
                same_location = True
                print("YES")
                break
    elif x2 > x1:
        while x2 > x1:
            x1 = x1+v1
            x2 = x2+v2
            if x1 == x2:
                same_location = True
                print("YES")
                break
    if not same_location:
        print("NO")
