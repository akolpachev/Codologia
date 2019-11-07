def time (x):
    hours = int(x/3600)
    print("часы: " + str(hours))
    mins = int((x-hours*3600)/60)    
    print("минуты: "+ str(mins))
    seconds = (x-hours*3600-mins*60) 
    print("секунды: "+ str(seconds))

print("введите секунды")
x=int(input())
time(x);

 

