import random
def vault_secrets():
    wrong = ["WRONG","You're hopeless...","Really, still here?","No, just no","Swing and a miss!","I told you, it won't work...","Is that actually your guess?","Nope","Give up, please","That tickles!","Try harder please", "Try harder please",
        "Don't make me angry",
        "You won't like me when im angry...",
        "Oh no, you just unlocked... NOTHING",
        "Just kidding, unlimited attempts",
        "Maybe you should do something else?",
        "This is getting ridiculous... [sic]",
        "Go collect some stars",
        "How about no?",
        "[PlayerName], please give up...",
        "Error, error. Bad answers.",
        "Failure", "May I suggest thinking"]
    b = "Might as well give you a riddle Since you insist on staying 'I have always been odd Remove my start and I am even When you complete this riddl I hope you are leaving Can you go now?"
    c = "Want to hear a secret?Just don't tell RubRub.I am building my own level.I call it 'The Challenge'.Hope it gets featured.But probably not...RubRub will never notice me"
    d = "Which came first?The chicken or the egg?...The egg, of course.Then the egg laid the chicken... and the chicken said.The password is on fire.I need to get some rest..."
    e = "Oh my head...I feel so drained.Would be nice to get some energy.You know, for my head...Nothing? OK..."
    f = ["I have heard about you","You think you can fool me","You are deeply mistaken","Go away!","I should have hid this room better...","You're not supposed to be in here...","RubRub won't like this...",
        "Don't touch that!","Why you touch my stuff?","RubRub better not find you in here...","Can't you just leave?","This is not the room you are looking for...","Sneaky sneaky...",
        "It's my precious...",
        "You shall not pass!",
        "Don't push the button!",
        "You're gonna get me in trouble...",
        "This is getting ridiculus... [sic]",
        "Go collect some stars",
        "Maybe there are new levels?",
        "Just, stop bothering me",
        "I'm gonna stop talking",
        "...",
        "......",
        "GAH!",
        "You're hopeless...",
        "Really, still here?",
        "Fine, press the button",e,d,c,b]



    print("\033[1;37;40m")
    A = input("Input : ")
    if A == "octucube":
        print("\033[1;27 Ugh... Slippery")
        vault_secrets()
    elif A == "seven":
        print("I should have been a doctor...")
        vault_secrets()
    elif A == "brainpower":
        print("O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo!")
        vault_secrets()
    elif A == "thechickenisonfire":
        print("Indeed it is...")
        vault_secrets()
    elif A == "gimmiethecolor":
        print("How many colors do you need?")
    elif A == "glubfub":
        print("NOOOO!! THIEF! THIEF!")
    elif A == "":
        H = random.choice(f)
        print(H)
        vault_secrets()
    elif A == "robtop":
        print("\033[1;31;40m RUBRUBRUBRUBRUB")
        vault_secrets()
    elif A == "kappa":
        print("\033[1;31;40m There is no kappa icon")
    elif A == "unicorn":
        print("\033[1;31;40m Why do they have a horn?")
        vault_secrets()
    elif A == "battop":
        print("\033[1;31;40m He could be watching us right now...")
        vault_secrets()
    elif A == "rubrubpowah123":
        print("\033[1;31;40m Ultimate Haxxor mode enabled.Not...")
        vault_secrets()
    else:
        G = random.choice(wrong)
        print("\033[1;31;40m",G)
        vault_secrets()
    

vault_secrets()