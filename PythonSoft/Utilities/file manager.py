print("FM is RUNNING!!!")
try:
    import os
    import time
    from tkinter import messagebox as msgbox
    import tkinter as tk
    import threading
    import shutil
    import psutil
except (ImportError, ModuleNotFoundError) as e:
    print(f"STOP: 0199/1002\nModule cannot be loaded, is not installed or contains errors. Make sure to check that the module is installed properly and check for disk corruption.\nDetails: {e}")
    input("Press ENTER to EXIT...")
    exit()
except Exception as e:
                print(f"Unhandled exception has occured in this program. Review the GitHub GamerSoft24/Software error chart for more info, as well as the Python Manual.\nDetails: {e}")
                input("Press ENTER to EXIT...")
                exit()
def clear():
    #return #uncomment for debugging
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def command():
    global runfl
    os.system(runfl)
def move2():
    global move1, to
    shutil.move(move1, to)
    input("Moved " + move1 + " to " + to + " with no errors. Press ENTER to continue...")
def copy2():
    global copy1, dest
    shutil.copy2(copy1, dest)
    input("Copied " + copy1 + " to " + dest + " with no errors. Press ENTER to continue...")
def fm(sdir):
    flag = True
    while flag == True:
            try:
                input("Press ENTER to continue...")
                clear()
                dshow = "dir " + sdir 
                os.system(dshow)
                valid = [1,2,3,4,5,6,7,8,9,10,11]
                print("*** FILE MANAGER VERSION 2 ***")
                print("Note: DIR = Directory / Folder")
                print("Operations :")
                print("[1] Change DIR")
                print("[2] Run file or command ")
                print("[3] Make FOLDER")
                print("[4] Make FILE")
                print("[5] Move FILES")
                print("[6] Copy FILES")
                print("[7] Rename FILE")
                print("[8] View disk information")
                print("[9] Delete DIR")
                print("[10] Delete FILE")
                print("[11] Exit")
                print("Current DIR : " + sdir)
                userchoice = int(input("Choose : "))
                print("Loading specified utility, please wait...")
                badchoice = True
                for x in range(len(valid)):
                    if valid[x] == userchoice:
                        badchoice = False
                        break
                if badchoice == True:
                    input("Invalid choice. Press ENTER to continue")
                if userchoice == 1:
                    sdir = input("Enter a VALID directory to change to : ")
                    input("DIR changed. Press ENTER to continue...")
                elif userchoice == 2:
                    global runfl
                    runfl = input("Enter a VALID file or command to run :")
                    threading.Thread(target=command).start()
                    
                elif userchoice == 3:
                    mkdir = input("Enter DIR file path/name (Example : C:\ST\TEST or /dev/sda/test) : ")
                    os.mkdir(mkdir)
                    input("DIR made with no errors. Press ENTER to continue...")
                elif userchoice == 4:
                    make = input("Enter a VALID file name to create (Example : C:\ST\TEST\TEST.TXT or /dev/sda/test/test.txt) : ")
                    with open(make,"x"):
                        input("File made with no errors. Press ENTER to continue...")
                elif userchoice == 5:
                    global move1, to
                    print("Moving files should not take very long. If it takes a long time, you may want to check your disks for errors")
                    move1 = input("From : ")
                    to = input("To : ")
                    threading.Thread(target=move2).start()
                elif userchoice == 6:
                    global copy1, dest
                    print("Copying files may take several minutes, please be aware")
                    copy1 = input("From : ")
                    dest = input("To : ")
                    threading.Thread(target=copy2).start()
                elif userchoice == 7:
                    filename = input("Please enter a valid file name or directory to rename (the full path must be included if the file is not in the same directory as this program): ")
                    newname = input("Enter a new name: ")
                    #os.system(f"ren {filename} {newname}") #old os.system handler
                    olddir = filename[:len(newname)] + "\\"
                    print(F"DEBUG: {olddir}")
                    os.rename(filename, olddir + newname)
                    input(f"Renamed {filename} to {olddir + newname} without errors. Press ENTER to continue...")
                elif userchoice == 8:
                    clear()
                    print("*** HARD DISK INFORMATIONS ***")
                    print("The program will read the disk information in alphabetical order (C:, D:), however it will not display certain informations if any disk is not ready (so if E: is not ready, F: will not display due to limitations of the psutil module)")
                    print("DRIVE | FILE SYSTEM |  SIZE  |  USED  |  FREE \n")
                    for x in psutil.disk_partitions():
                        try:
                                usage = psutil.disk_usage(x.mountpoint)
                                print(f"{x.mountpoint}     {x.fstype}          {usage.total/(1024**3):.2f} {usage.used/(1024**3):.2f} {usage.free/(1024**3):.2f}\n")
                            
                        except PermissionError as e:
                            if 'not ready' in str(e):
                                print(f"{x.mountpoint}     Disk not ready for reading")
                                continue
                                
                            print(f"STOP: 0210\nAccess violation trying to read disk information. Make sure you have the permissions to use all disks, then try again.\nDetails: {e}")
                            
                        except Exception as e:
                            print(f"Unhandled exception has occured in this program. Review the GitHub GamerSoft24/Software error chart for more info, as well as the Python Manual.\nDetails: {e}")
                            
                elif userchoice == 9:
                    rmdir = input("Enter DIR to remove (this will remove all files in directory as well) : ")
                    if input(f"{rmdir} and its contents will be permanently deleted! Proceed with operation? [Y/N]: ") == "Y":
                        shutil.rmtree(rmdir)
                        input("Removed DIR with no errors. Press ENTER to continue...")
                elif userchoice == 10:
                    rmf = input("Enter FILE to remove : ")
                    if input(f"{rmf} will be permanently deleted! Proceed with operation? [Y/N]: ") == "Y":
                        os.remove(rmf)
                        input("Removed File with no errors. Press ENTER to continue...")
                elif userchoice == 11:
                    exit()
            except PermissionError as e:
                print(f"STOP : 0210\nAccess violation in file. Make sure that you have the permissions to use the file, then try again.\nDetails: {e}")
            except FileNotFoundError as e:
                print(f"STOP: 6510B\nValid file or folder specified is not valid or could not be found. Make sure you spelled it correctly, then try again\nDetails: {e}") 
                
            except EOFError:
                print("STOP : 0250\nUser has chosen to exit. Exiting...")
                exit()
            except ValueError as e:
                print(f"STOP : 0211\nBad value was specified (e.g a letter when asked for a number or code is invalid. Enter the CORRECT values that are demanded, then try again.\nDetails: {e}")
                
            except KeyboardInterrupt:
                print("STOP : 0270\nUser has chosen to exit. Exiting...")
                exit()
            except SystemExit:
                print("User has chosen to exit. Exiting...")
                exit()
            except IOError as e:
                print(f"STOP : 0272\nI/O Error. A device attached to the system malfunctioned or has been unplugged during an operation. Check all drives and ports for loose connections or errors, and use Safe Eject whenever possible\nDetails: {e}")
                input("Press ENTER to EXIT...")
                exit()
            except threading.ThreadError as e:
                print(f"Unhandled exception has occured in this program. Review the GitHub GamerSoft24/Software error chart for more info, as well as the Python Manual.\nDetails: {e}")
                
                fm(sdir)
            except Exception as e:
                print(f"Unhandled exception has occured in this program. Review the GitHub GamerSoft24/Software error chart for more info, as well as the Python Manual.\nDetails: {e}")
                
                fm(sdir)
print("WARNING!This is an UNSTABLE release.Crashes are to be EXPECTED and this program is best suited to PROFESSIONAL users.To avoid CRASHES,please only use valid file names.")
fm(input("Starting DIR : "))
