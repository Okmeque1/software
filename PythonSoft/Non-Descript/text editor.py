import os
try:
    flag = True
    while flag == True:
        print("Text editor version 1 Revision 1A")
        print("The creator of this program is Okmeque1")
        print("Select one of the following")
        print("1 : Create a new file")
        print("2 : Add bytes to file")
        print("3 : Erase file")
        print("4 : Delete file")
        print("This program will accept any files but may not be able to read from all file formats.Supported file types are .md and .txt.Your mileage may vary depending on the file format you use.")
        a = input("Choose an option(any invalid option to abort.) : ")
        if a == "1":
            filename = input("Please enter your desired file name for file. The format must be 'A:\directory\subdirectory\file.txt' : ")
            with open(filename,"x") as b:
                print("File created with no errors.Returning to main screen")
        elif a == "2":
            filename0 = input("Please enter the desired file name of the file for editing.The format must be 'A:\directory\subdirectory\file.txt' : ")
            with open(filename0,"a") as c:
                write = True
                while write == True:
                    d = input("Enter whatever you like into the file.This will be added on top of the existing bytes.Type 'eX1t' to return to the main screen : ")
                    if d == "eX1t":
                        print("You have chosen to quit and are now being returned to the main screen")
                        write = False
                    else:
                        c.write(d)
        elif a == "3":
            filedelete = input("Please enter the desired filename to erase. The format must be 'A:\directory\subdirectory\file.txt' : ")
            with open(filedelete,"w") as e:
                warn = input("ALL DATA IN FILE WILL BE LOST!Do you wish to continue?(YES,any invalid option to deny.)")
                if warn == "YES":
                    confirmation = input("This is an IRREVERSIBLE decision.Do you wish to proceed?(YES,any invalid option to deny.)")
                    if confirmation == "YES":
                        g = "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 "
                        e.write(g) 
                        print("File erased") 
                    else:
                        print("Action Aborted.")
                else:
                    print("Action aborted")  
        elif a == "4":
            fileerase = input("Enter the desired file name to delete.The format must be 'A:\directory\subdirectory\file.txt' : ")
            warn = input("ALL DATA IN FILE WILL BE LOST!Do you wish to continue?(YES,any invalid option to deny.)")
            if warn == "YES":
                confirmation = input("This is an IRREVERSIBLE decision.Do you wish to proceed?(YES,any invalid option to deny.)")
                if confirmation == "YES":
                    os.remove(fileerase)
                else:
                    print("Action Aborted")
            else:
                print("Action Aborted")
        else:
            flag = False
except FileNotFoundError:
        print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
        input("Press ENTER to exit.")
        exit()
except PermissionError:
    print("STOP : 0210\nThe OS cannot perform this operation.You may not have the appropriate permissions to do such actions.")
    input("Press ENTER to exit...")
    exit()
except KeyboardInterrupt or EOFError:
        print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
        exit()
