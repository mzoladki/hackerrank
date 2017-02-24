#!/bin/python3

import sys


def x_factor_b(tab, x):
    num = 0
    for y in tab:
        if y % x == 0:
            num += 1
    if num == len(tab):
        return True
    else:
        return False


def a_factor_x(tab, x):
    num = 0
    for y in tab:
        if x % y == 0:
            num += 1
    if num == len(tab):
        return True
    else:
        return False


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

a.sort()
b.sort()

count = 0

for i in range(1, 101):
    if x_factor_b(b, i):
        if a_factor_x(a, i):
            count += 1

print(count)
