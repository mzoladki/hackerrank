a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
A = [a0, a1, a2]
B = [b0, b1, b2]
Alice=0
Bob=0
for i in range(len(A)):
    if A[i]>B[i]:
        Alice += 1
    elif A[i]<B[i]:
        Bob += 1
    else:
        pass

