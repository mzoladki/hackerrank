n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

left = 0
right = 0
x = n-1

for i in range(n):
    left += a[i][i]
    right += a[x][i]
    x -= 1

print(abs(right - left))

