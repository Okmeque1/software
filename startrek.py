import random

num = random.choice([1,2,3,4,5,6])


def dés(score):
    num = random.choice([1,2,3,4,5,6])
    score = score + num
    print(num)
    if num == 1:
        print("You lost")
        print("The score is " + str(score))
        return
    else:
        print("Do you want to continue?[Y,N]")
        a = input("")
        if a == "N":
            print("The score is " + str(score) + ".The game has ended")
        if a == "Y":
            print("Score saved.You will see the score when you lose.")
            dés(score)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
 
dés(0)



def dés1(score):
             num = random.choice([1,2,3,4,5,6])
             score = score + num
             print(num)
             print("The score is " + str(score))
             if num == 1:
                 print("You lost")
                 print("The score is 0")
                 return
             else:
                 print("Do you want to continue?[Y,N]")
                 a = input("")
                 if a == "N":
                     print("The score is " + str(score) + ".The game has ended")
                 if a == "Y":
                     
                     dés1(score)
                     
                     
                     
