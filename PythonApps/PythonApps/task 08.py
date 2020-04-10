def change (x,key,value):
    if key in x:
        x[key] = value
    
x={}

print("введите ключ и значение")

for i in range(3):
    key = input("ключ: ")
    value = input("значение: ")
    x[key] = value

print(x)

print("введите ключ и новое значение ")
change(x,input("ключ: "),input("значение: "))

print(x)