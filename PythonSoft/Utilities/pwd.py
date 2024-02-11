import random 
try:
    flag = True
    print("****THE OPEN SOURCE PASSWORD SECURITY SYSTEM****")
    print("Program version 1.2.0. Made by Okmeque1")
    while flag == True:
        print("Affiliate company © TCG - Technology, Coding and Gaming Inc ™")
        print("1 -> Add or generate password to save file.")
        print("2 -> Retrieve password from save file.")
        print("3 -> Format save file")
        print("4 -> More info.")
        print("5 -> Advanced password generator.")
        print("6 -> Change password")
        print("7 -> Save and quit")
        print("When you are asked a valid file name,please make sure that the directory is valid and for best compatability,please make sure that the file already exists.")
        print("If you are a non-technical user,please choose option 4 before proceeding as it tells you about filepaths,OS compatability and more.")
        print("This is an open-source program so you can share it anywhere on the internet,USB/CD/DVD or other media.Please mention in your copy Okmeque1 so that the original code is not lost to time.")
        option = int(input("Select option : "))
        if option == 1:


            print('Welcome to your password generator')

            chars = '¦¬`1!23£4$€5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'

            number = 1

            length = input('Password length ')
            length = int(length)
            


            for pwd in range(number):
                passwords = ''
                for c in range(length):
                    passwords += random.choice(chars)
                    
                    print("You are at " + str(c) + " of " + str(length) + " complete.")
                print("")
                print(passwords)
                print("")
                print('Passwords Generated.Saving...')
                filename = input("Please enter a valid file name (none to default of G:\python\demo\demo.pc). The format must be a:\directory\pwdfile.extention. : ")
                if filename == "":
                    filename = "G:\python\demo\demo.pc"
                    set0 = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                    passave = open(filename,"a")
                    passave.write(set0 + " -> " + passwords + "\n")
                    passave.close()
                else:
                    set0 = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                    passave = open(filename,"a")
                    passave.write(set0 + " -> " + passwords + "\n")
                    passave.close()
                print("Save has completed with no disk errors.")
                print("Now returning to the main menu")
        elif option == 2:
            fileopen = input("Please enter a valid file name (none to default of G:\python\demo\demo.pc). The format must be a:\directory\pwdfile.extention. : ")
            if fileopen == "":
                fileopen = "G:\python\demo\demo.pc"
                passopen = open(fileopen,"r")
                set1 = input("Please enter the set name for the desired password. : ")
                for line in passopen:
                    if line.split(" -> ")[0] == set1:
                        print(line.split(" -> ")[1])
            else:
                passopen  = open(fileopen,"r")
                set1 = input("Please enter the set name for the desired password. : ")
                for line in passopen:
                    if line.split(" -> ")[0] == set1:
                        print(line.split(" -> ")[1])
        elif option == 3:
            password = input("This is an IRREVERSIBLE decision as you may corrupt files if used incorrectly.You may now enter your password → ")
            with open("g:\python\demo\okmeque1.txt","r") as passchk:
                passchk0 = passchk.readlines()
        
            if passchk0[0] == password:
                del1 = input("Press enter to continue...")
                filedel = input("Please enter a valid file name.The format for the file must be a:\directory\pwdfile.extention : ")
                if del1 == "":
                    with open(filedel,"r") as read0:
                        read = read0.readlines()
                    with open(filedel,"w") as passdelete:
                        del2 = input("Enter set name : ")
                        for line in read:
                            if line.split(" -> ")[0] != del2:
                                passdelete.write(line)
                                print("Set overwritten with value of none.")

            else:
                print("An error has occured.To continue,")
                print(" → Press enter to return to the main menu")
                print(" → Press CTRL + C to terminate this program.You will lose any unsaved data in any open programs.")
                print("Press any ENTER to continue.Error : 0FA3E22")
                input("")
        elif option == 4:
            print("\n")
            print("This program is open source and made by Okmeque1.If you desire to copy this program,please keep a mention of Okmeque1 in the code as so the original code is not lost to time.")
            print("This program can create a secure password of your length,8 to 19 characters is recommended for a secure password(DO NOT MAKE YOUR PASSWORD TOO LONG AS IT CAN OVERLOAD THE BUFFER ON THE COMPUTER AND CRASH IT.),can retrieve the password(this function is only useful if the file extention is foreign) and can erase the password file in case of hacking")
            print("You may change the program defaults on line 37,39,53 and 55.(If you want to do this,you must change the defaults on ALL of the lines to ensure maximum compatability and change the input str to the default set in the none → default variable)")
            print("For maximum compatability,run this program in Python 3+ and Windows 7 or higher(Please note that you can run it lower than those versions but the program might throw errors in lower version of windows(XP,Vista,etc) and some python functions might not exist in lower versions of python)")
            print("The program will run on macOS and Linux but the filepath format will vary as neither of those use drive letters (eg A:\directory\file.ext).The structure for those OS's will either be : ")
            print("1 : macOS : The file structure may be /path/path1/pwdfile.extention")
            print("2 : Linux : The file structure is unclear as there are so many Linux distros out there but the structure may be /dev/sda/mountpoint1/folder/pwdfile.extention.")
            print("Please note that in both cases,DO NOT USE FOREIGN FILE EXTENTIONS(.dell,pc or any non-standard file format that can't be read by a text editor.) as the disk check utility might assume that the file is corrupt and delete it.")
            print("Please do NOT modify this program as the file may become unoriginal and might cause program breakage.This program took HOURS to complete and be at its current state.\n")
            input("Press enter to continue")
        elif option == 5:
            end = ""
            passwd = ""
            spc = '¦¬`!£$€%^&*()-_=+;:@~#\|,<.>/?'
            num = "1234657890"
            ch = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmMm"
            spcs = ""
            nums = ""
            chs = ""
            spcn = int(input("Enter special character count : "))
            numn = int(input("Enter number count : "))
            chn = int(input("Enter standard character count : "))
            for p in range(spcn):
                spcs += random.choice(spc)
            for s in range(numn):
                nums += random.choice(num)
            for ad in range(chn):
                chs += random.choice(ch)
            end += spcs + nums + chs
            for x in range(len(end)):
                passwd += random.choice(end)
            print(passwd)
            filenam = input("Please enter a valid file name (none to default of G:\python\demo\demo.pc). The format must be a:\directory\pwdfile.extention. : ")
            if filenam == "":
                filenam = "G:\python\demo\demo.pc"
                sets = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                passavee = open(filenam,"a")
                passavee.write(sets + " -> " + passwd + "\n")
                passavee.close()
            else:
                sets = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                passavee = open(filenam,"a")
                passavee.write(sets + " -> " + passwd + "\n")
                passavee.close()
            print("Save has completed with no disk errors.")
            print("Now returning to the main menu")
        elif option == 6:
                filedels = input("Please enter a valid file name. The format for the file must be a:\directory\pwdfile.extention : ")
                sets1 = input("Enter SET name to change : ")

                with open(filedels,"r") as readpwd:
                    r1 = readpwd.readlines()
                    for b in range(len(r1)):
                        if r1[b].strip("\n").split(" -> ")[0] == sets1:
                            setnarme = r1[b].strip("\n").split(" -> ")[0] + " -> "
                            newpwd = input("Enter new password : ")
                            newsetpwd = setnarme + newpwd + "\n"
                            r1[b] = newsetpwd
                with open(filedels,"w") as changepwd:
                    for a in range(len(r1)):
                        changepwd.writelines(r1[a])
                print("Save completed with no disk errors. Returning to main menu...")
        elif option == 7:
            print("You have quit this program and you are now in a command processor.Please quit the command processor if you do not know or want to use it.")
            flag = False    

        


    def randomchr():
        for _ in range(100001):
            print(random.choice(chars))
            
    def storage():
        return 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv'

    def passw():
        pass1 = input('Enter password ')
        if pass1 == 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv':
            print('You found the secret PWD')
            def secret1():
                print('Use  the function storage() to get access to this again')
            secret1()
        else:
            pass2 = input('Enter password ')
            if pass2 == 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv':
                print('You found the secret PWD')
                def secret1():
                    print('Use  the function storage() to get access to this again')
                    
            else:
                return 'You lost!'
except FileNotFoundError:
        print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
        input("Press ENTER to exit.")
        exit()
except KeyboardInterrupt or EOFError:
        print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
        exit()

""
