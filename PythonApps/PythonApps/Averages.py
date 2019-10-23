from random import randint

N=10
A=[0]*N

# fill array
for i in range(N):
    A[i]=randint(0, 100)
    print(A[i])


# calculate values
print("Average:")
X1=0
X2=0
Y1=0
Y2=0

for i in range(N):    
    if A[i]<50:
        X1=X1+A[i]
        X2=X2+1
    else:
        Y1=Y1+A[i]
        Y2=Y2+1

print("<50: " + str(X1) + "/" + str(X2) + " = " + str(X1/X2))
print(">=50: " + str(Y1) + "/" + str(Y2) + " = " + str(Y1/Y2))
   


