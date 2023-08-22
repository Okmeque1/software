import random
import os
B = 1
wrong = True
print("HANG-MAN - Okmeque1 edition")
file = input("Please enter a valid file name (none to default of G:\python\demo\words.txt). The format must be a:\directory\wordfile.txt : ")
if file == "":
    file = "G:\python\demo\words.txt"
fileopen = open(file,"r")
ninety = []
w = ["WRONG","No, just no","Swing and a miss!","Error, error. Bad answers.","Failure"]
for line in fileopen:
    ninety.append(line.strip())
RC = random.choice(ninety)
c = [""]
c = c * (len(RC))
d = 0
while B == 1:
    print(c)
    wrong = True
        
    A = input("Enter letter." + str(len(RC)) + " is the length of this word : ")
    
    for i in range(len(RC)):
        if A == RC[i]:
            print("Correct at ",i)
            wrong = False
            c[i] = A 

    if "".join(c) == RC:
        print("Game won!")
        print("The word was : " + RC)
        B = 2

    if wrong == True:
        print(random.choice(w))
        d = d + 1
        print("Failed : " + str(d))
    if d == 7:
        print("WARNING!You are at 7 failed attempts.At 8 failed attempts the computer will terminate this program!.")
    elif d == 8:
        print("You lost! The word was " + RC)
        B = 2
