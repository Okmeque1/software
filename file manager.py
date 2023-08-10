import os
import time
from tkinter import messagebox as msgbox
import tkinter as tk
def icmd():
    fg = True
    print("ICMD Version 1.00")
    while fg == True:
        prompt = input(">")
        os.system(prompt)
    exit()
def fm(sdir):
    try:
        dshow = "dir " + sdir + " /p"
        os.system(dshow)
        valid = [1,2,3,4,5,6,7,8,9]
        print("Operations :")
        print("[1] Change DIR")
        print("[2] Run file ")
        print("[3] Make FOLDER")
        print("[4] Make FILE")
        print("[5] Move FILES")
        print("[6] Copy FILES")
        print("[7] Enter internal CMD")
        print("[8] Enter CMD.EXE")
        print("[9] Exit")
        userchoice = int(input("Choose : "))
        if userchoice == 1:
            chdir = input("Enter a VALID directory to change to : ")
            sdir = chdir
            fm(sdir)
        elif userchoice == 2:
            runfl = input("Enter a VALID file to run :")
            os.system(runfl)
            fm(sdir)
        elif userchoice == 3:
            mkdir = input("Enter DIR file path/name(Example : C:\ST\TEST) : ")
            mkdir0 = "mkdir " + mkdir
            os.system(mkdir0)
            fm(sdir)
        elif userchoice == 4:
            make = input("Enter a VALID file name to create(Example : C:\ST\TEST\TEST.TXT) : ")
            with open(make,"x"):
                print("Success")
                fm(sdir)
        elif userchoice == 5:
            move = input("From : ")
            to = input("To : ")
            moveto = "move " + move + " " + to
            os.system(moveto)
            fm(sdir)
        elif userchoice == 6:
            copy = input("From : ")
            dest = input("To : ")
            copyto = "copy " + copy + " " + dest
            os.system(copyto)
        elif userchoice == 7:
            icmd()
        elif userchoice == 8:
            os.system("C:\Windows\System32\CMD.EXE")
        elif userchoice == 9:
            exit()
    except FileNotFoundError:
        sev = tk.Tk()
        sev.withdraw()
        severe = msgbox.showerror("Severe","You must specify a valid file/folder.")
        fm(sdir)
    except EOFError:
        print("You have raised EOFError and will now exit.Details : User raised EOFError unexpectedly which was caught by an except block.")
        exit()
    except ValueError:
        input("Invalid parameter.Acceptable values are from 1-9.Press ENTER to continue...")
        fm(sdir)
    except KeyboardInterrupt:
        print("KeyboardInterrupt called.Now exiting...")
        exit()
    except:
        input("An unexpected error occured.Press ENTER to continue...")
        fm(sdir)
print("WARNING!This is an UNSTABLE release.Crashes are to be EXPECTED and this program is best suited to PROFESSIONAL users.To avoid CRASHES,please only use valid file names.")
fm(input("Starting DIR : "))