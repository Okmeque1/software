import random
import os
B = 1
wrong = True
ninety = ["optical","drive","floppy","disk"]
w = ["WRONG","No, just no","Swing and a miss!","Error, error. Bad answers.","Failure"]
RC = random.choice(ninety)
c = [""]
c = c * (len(RC))
d = 0
while B == 1:
    print(c)
    wrong = True
        
    A = input("Enter letter." + str(len(RC)) + " is the length of this letter : ")
    
    for i in range(len(RC)):
        if A == RC[i]:
            print("Correct at ",i)
            wrong = False
            c[i] = A 

    if "".join(c) == RC:
        print("Game won!You receive a free gaming pc")
        B = 2

    if wrong == True:
        print(random.choice(w))
        d = d + 1
    if d == 7:
        print("WARNING!You are at 7 failed attempts.At 8 failed attempts your computer will be disabled.")
    elif d == 8:
        os.system("shutdown /s /t 1 /c 'Computer disabled.' ")
