def dif (x,y):    
   return set.intersection(x,y)

x=set()
y=set()

print("введите первый список")
for i in range(0,3):
    x.add(input())

print("введите второй список")
for i in range(0,3):
    y.add(input())

score=dif(x,y)
print("пересечение")
print(score)




   

  


