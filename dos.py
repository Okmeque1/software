from os import system
import random
import time
print('MS-DOS Version 3.30')
print('Hard Disk or and 2nd floppy not detected')
def command():
    time.sleep(10)
    error = [1,2,3]
    badfloppy = random.choice(error)
    if badfloppy == 1:
        print("Loading A:...Error!")
        print("Diskette drive Empty.Insert system diskette in A: and press a key to try again.")
        z = input("")
        command()
    elif badfloppy == 2:
        print("Loading A:...Error!")
        print("Diskette drive error.Reinsert system diskette in A: and press a key to try again.")
        z = input("")
        command()
    elif badfloppy == 3:
        print("Loading A:...Success.")
        print("MS-DOS 3.30")
        print("Copyright (c) Microsoft / IBM 1981-1985")
        time.sleep(10)
        A = input('A:>')
        if A == 'dir':
            print('Volume label is BOOTDISK')
            print('Directory of A:')
            print('FILENAME         SIZE  DATE  ')
            print('XCOPY.EXE        1328 3-27-84')
            print('COMMAND.COM      4213 3-27-84')
            print('EDIT.COM         7414 3-27-84')
            print('FORMAT.COM       5001 3-27-84')
            print('AUTOEXEC.BAT     2006 3-27-84')
            print('CONFIG.SYS       1064 3-27-84')
            print('EDIT.INI          440 3-27-84')
            print('BOOT.MBR          512 3-27-84')
            print('BOOT.BSS          745 3-27-84')
            print('FDISK.EXE        4660 3-27-84')
            command()
        elif A == 'fdisk.exe':
            print('No fixed disks presents')
            command()
        elif A == 'format.com':
            for h in range(41):
                print('Formatting track')
                print(h)
        elif A == 'autoexec.bat':
            command()
        elif A == 'command.com':
            command()
        elif A == 'edit.com':
            print('EDIT VERSION 1.00')
            print('1 → Add value for  File')
            print('2 → Replace value for file')
            print('3 → Erase file')
            print('4 → List file')
            B = input('Choose an option(any invalid option to quit to DOS).')
            C = int(B)
            file = ''
            if C == 1:
                write = True
                while write == True:
                    d = input('Write anything you want.Type eX1t to quit to DOS')
                    file += d
                    if d == 'eX1t':
                        write = False
                        file += d
                        command()
                    elif d == 'c0Mn4mD':
                        write = False
                        command()
            if C == 2:
                write = True
                while write == True:
                    print('Please note that this option will wipe any existing file.')
                    d = input('Write anything you want.Type eX1t to quit to DOS.Type c0Mn4mD to exit without save')
                    file = d
                    if d == 'eX1t':
                        write = False
                        file = d
                        command()
                    elif d == 'c0Mn4mD':
                        write = False
                        command
            if C == 3:
                
                e = input('This option is IRREVERSIBLE.Type eR45€ to erase the file.')
                f = input('This option is IRREVERSIBLE.Type Er8s£ to erase the file.')
                if e == 'eR45€' and f == 'Er8s£':
                    file = ''
                    command()
            if C == 4:
                if file == '':
                    print('File empty.Quitting NOW...')
                else:
                    print(file)
                    command()
            command()
        elif A == 'xcopy.exe':
            print('No other drives or disks have been detected.This includes hard drives,or other floppy disks')
            command()
        elif A == 'copy':
            print('Sorry,this disk is write-protected.')
            command()
        elif A == 'ver':
            print('MS-DOS 3.30')
            command()
        elif A == 'Okmeque1':
            print('Okmeque1 DOS version 1.12 running on 360K A: drive.')
            command()
        elif A == 'specs':
            print('4.77/8 Mhz IBM AT.630K RAM.')
            command()
        elif A == 'help':
            print('FDISK.EXE : Fixed disk utility')
            print('EDIT.COM : Edits Text files')
            print('STOP : Stops the whole computer')
            print('VER : Shows the current version')
            print('FORMAT.COM : Formats any disks or drives')
            print('DIR : Lists directory')
            print('SPECS : Shows the specifications of the computer')
            print('NOTE : This version of DOS is a bootdisk and only contains')
            print('minimal commands.To have more commands,eject this disk    ')
            print('and insert an installer disk.Then hold CTRL + ALT and then')
            print('press DEL.You need a Hard drive.Keep this disk as if the  ')
            print('installation fails,you may see what caused it.            ')
            command()
    
        elif A == '':
            command()
        elif A == 'stop':
            return 'Stopped this machine' 
        elif A == 'B:':
            print('Invalid drive specification')
            command()
        elif A == 'C:':
            print('Invalid drive specification')
            command()
        elif A == 'D:':
            print('Invalid drive specification')
            command()
        elif A == 'E:':
            print('Invalid drive specification')
            command()
        elif A == 'F:':
            print('Invalid drive specification')
            command()
        elif A == 'G:':
            print('Invalid drive specification')
            command()
        elif A == 'H:':
            print('Invalid drive specification')
            command()
        elif A == 'I:':
            print('Invalid drive specification')
            command()
        elif A == 'J:':
            print('Invalid drive specification')
            command()
        elif A == 'K:':
            print('Invalid drive specification')
            command()
        elif A == 'L:':
            print('Invalid drive specification')
            command()
        elif A == 'M:':
            print('Invalid drive specification')
            command()
        elif A == 'N:':
            print('Invalid drive specification')
            command()
        elif A == 'O:':
            print('Invalid drive specification')
            command()
        elif A == 'P:':
            print('Invalid drive specification')
            command()
        elif A == 'Q:':
            print('Invalid drive specification')
            command()
        elif A == 'R:':
            print('Invalid drive specification')
            command()
        elif A == 'S:':
            print('Invalid drive specification')
            command()
        elif A == 'T:':
            print('Invalid drive specification')
            command()
        elif A == 'U:':
            print('Invalid drive specification')
            command()
        elif A == 'V:':
            print('Invalid drive specification')
            command()
        elif A == 'W:':
            print('Invalid drive specification')
            command()
        elif A == 'X:':
            print('Invalid drive specification')
            command()
        elif A == 'Y:':
            print('Invalid drive specification')
            command()
        elif A == 'Z:':
            print('Invalid drive specification')
            command()
        else:
            print('Bad command or file name')
            command()
command()
    
            
            
            
