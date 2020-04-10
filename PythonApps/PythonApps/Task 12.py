import random
keep_going = True
while keep_going:

    dice =[0,0,0,0,0]
    
    for i in range(5):

         dice[i] = random.randint(1,6)
    print("вам выпало:",dice)
    if dice[0] == dice[4]:
         print("яцзы")
    elif (dice[0]==dice[3]) or (dice[1]==dice[4]):
         print("четыре одинаковых")
    
    elif(dice[0]==dice[2]) or (dice[1]==dice[3]) or (dice[2]==dice[4]):
         print("три одинаковые")

    keep_going=(input("нажмите enter для продолжения,любую клавишу чтобы выйти:")=="")



























    
