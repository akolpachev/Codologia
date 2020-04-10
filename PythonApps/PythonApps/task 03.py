from random import randint
print("Введите N")
N=int(input())

A=[0]*N
for i in range(N):
    A[i]=randint(0, 1)
    print(A[i], end='')

print()
    
for i in range(N):
    if A[i]==0:
        print(1, end="")
    if A[i]==1:
        print(0, end="")

print()






