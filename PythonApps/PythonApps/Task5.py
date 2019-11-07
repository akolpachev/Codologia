s=[]
for i in range (0,5):
    x=input()
    s.append(x)

print()    
print("min: " + min(s, key=len))
print("max: " + max(s, key=len))

