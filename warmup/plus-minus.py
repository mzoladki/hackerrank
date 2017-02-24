n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positive = 0
negative = 0
zeros = 0
for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zeros += 1

print(positive/n)
print(negative/n)
print(zeros/n)
