import random
def u1(cpts,pts,rnd):
    if rnd == 1 or rnd == 2 or rnd == 5:
        input("Nothing happened.Press ENTER to continue")
        rps(cpts,pts)
    elif rnd == 3 or rnd == 6:
        print("Player 1 has won a point!")
        pts += 1
        rps(cpts,pts)
    elif rnd == 4:
        print("Computer 1 has won a point!")
        cpts += 1
        rps(cpts,pts)
def u2(cpts,pts,rnd):
    if rnd == 1 or rnd == 5 or rnd == 2:
        input("Nothing happened.Press ENTER to continue")
        rps(cpts,pts)
    elif rnd == 3 or rnd == 6:
        print("Computer 1 has won a point!")
        cpts += 1
        rps(cpts,pts)
    elif rnd == 4:
        print("Player 1 has won a point!")
        pts += 1
        rps(cpts,pts)
def u3(cpts,pts,rnd):
    if rnd == 1 or rnd == 6 or rnd == 5:
        print("Computer 1 has won a point!")
        cpts += 1
        rps(cpts,pts)
    elif rnd == 3 or rnd == 4:
        input("Nothing happened.Press ENTER to continue")
        rps(cpts,pts)
    elif rnd == 2:
        print("Player 1 has won a point!")
        pts += 1
        rps(cpts,pts)
def u4(cpts,pts,rnd):
    if rnd == 3 or rnd == 4 or rnd == 5 or rnd == 6:
        input("Nothing happened.Press ENTER to continue")
        rps(cpts,pts)
    elif rnd == 1:
        print("Player 1 has won a point!")
        pts += 1
        rps(cpts,pts)
    elif rnd == 2:
        print("Computer 1 has won a point!")
        cpts += 1
        rps(cpts,pts)
def u5(cpts,pts,rnd):
    if rnd == 2 or rnd == 4 or rnd == 5:
        input("Nothing happened.Press ENTER to continue")
        rps(cpts,pts)
    elif rnd == 3 or rnd == 1:
        print("Player 1 has won a point!")
        pts += 1
        rps(cpts,pts)
    elif rnd == 6:
        print("Computer 1 has won a point!")
        cpts += 1
        rps(cpts,pts)
def u6(cpts,pts,rnd):
    if rnd == 3 or rnd == 4 or rnd == 6:
        input("Nothing happened.Pres ENTER to continue")
        rps(cpts,pts)
    elif rnd == 1:
        print("Computer 1 has won a point!")
        cpts += 1
        rps(cpts,pts)
    elif rnd == 2 or rnd == 5:
        print("Player 1 has won a point!")
        pts += 1
        rps(cpts,pts)
def whowin(cpts,pts):
    if pts >= cpts:
        print("Player 1 has won!")
        exit()
    else:
        print("Computer 1 has won!")
        exit()
def rps(cpts,pts):
    if cpts == 10 or pts == 10:
        whowin(cpts,pts)
    print("Computer points : " + str(cpts))
    print("Player points : " + str(pts))
    rn = [1,2,3,4,5,6]
    uchoice = input("Enter 1,2,3,4,5,6 = ")
    rf = random.choice(rn)
    if uchoice == "1":
        u1(cpts,pts,rf)
    elif uchoice == "2":
        u2(cpts,pts,rf)
    elif uchoice == "3":
        u3(cpts,pts,rf)
    elif uchoice == "4":
        u4(cpts,pts,rf)
    elif uchoice == "5":
        u5(cpts,pts,rf)
    elif uchoice == "6":
        u6(cpts,pts,rf)
    else:
        rps(cpts,pts)
def start():
    print("***RPS - Okmeque1 Edition***")
    print("The INPUT will be shown like this : Enter 1,2,3,4,5,6,any other option to return to start = ")
    print("READ THIS CAREFULLY!!!")
    print("1 = ROCK")
    print("2 = PAPER")
    print("3 = SCISSORS")
    print("4 = ROCK MINER")
    print("5 = CARDBOARD")
    print("6 = BOX KNIFE")
    input("Press ENTER to continue")
    print("UNCONVENTIONAL RULE SET :")
    print("1 = ROCK can break SCISSORS or BOX KNIFE")
    print("2 = PAPER can break ROCK MINER only.")
    print("3 = SCISSORS can break PAPER only.")
    print("4 = ROCK MINER can break ROCK only.")
    print("5 = CARDBOARD can break ROCK and SCISSORS")
    print("6 = BOX KNIFE can break PAPER and CARDBOARD")
    input("Press ENTER to start the game")
    rps(0,0)
start()