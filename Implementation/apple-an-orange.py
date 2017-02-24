#!/bin/python3

import sys


s, t = input().strip().split(' ')
home = [int(s), int(t)]

a, b = input().strip().split(' ')
trees = [int(a), int(b)]

m, n = input().strip().split(' ')
distances = [int(m), int(n)]

apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

number_of_apples = 0
number_of_oranges = 0

for i in apple:
    #print("apple falls at:", trees[0] + i)
    if (trees[0] + i >= home[0]) and (trees[0] + i <= home[1]):
        number_of_apples += 1

for i in orange:
    #print("orange falls at:", trees[1] + i)
    if (trees[1] + i <= home[1]) and (trees[1] + i >= home[0]):
        number_of_oranges += 1

print(number_of_apples)
print(number_of_oranges)
