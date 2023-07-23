import os
import random
import time
def boot():
    os.system("title DOS - Windows Virtual Machine")
    print("THE WINDOWS VIRTUAL BIOS VERSION 3.20")
    print("DRIVER WAS NOT INSTALLED.CD-ROM DRIVE NOT FOUND")
    print("No fixed disks detected.")
    print("327680B OK")
    print("Loading C...Not loaded.")
    print("No fixed disks detected.")
    time.sleep(10)
    error = [1,2,3,4,5,6,7,8,9]
    badfloppy = random.choice(error)
    if badfloppy == 1:
        print("Loading A:...Error!")
        print("Diskette drive Empty.Insert system diskette in A: and press a key to try again.")
        z = input("")
        boot()
    elif badfloppy == 2:
        print("Loading A:...Error!")
        print("Diskette drive error.Reinsert system diskette in A: and press a key to try again.")
        z = input("")
        boot()
    elif badfloppy == 3:
        print("Invalid system disk")
        print("Replace the disk and press any key...")
        z = input("")
        boot()
    elif badfloppy == 4:
        print("Reboot and Select proper Boot device")
        print("or Insert Boot media in selected boot device and press a key")
        z = input("")
        boot()
    elif badfloppy == 5:
        print("Loading A:...Success.")
        print("MS-DOS 3.30")
        print("Copyright (c) Microsoft / IBM 1981-1985")
        print("The following file is missing or corrupt : BOOT.MBR")
        print("The following file is missing or corrupt : BOOT.BSS")
        print("There is an error in your CONFIG.SYS on line 37.")
        print("While initializing device IOS:")
        print(" A subsystem driver failed to load. \n \n")

        print("Either a file in the .\iosubsys")
        print("subdirectory is corrupt, or the system is low on memory.")
        print("DOS Failed to load.Press any key to reboot the machine.")
        z = input("")
        boot()
    elif badfloppy == 6 or badfloppy == 7 or badfloppy == 8 or badfloppy == 9:
        print("Loading A:...Success.")
        print("MS-DOS 3.30")
        print("Copyright (c) Microsoft / IBM 1981-1985")
        print("Initializing sound device...")
        time.sleep(10)
        command()
def command():
        A = input('A>')
        if A == 'dir':
            print('Volume label is BOOTDISK')
            print('Directory of A:')
            print('FILENAME         SIZE  DATE  ')
            print('XCOPY.EXE        1328 3-27-84')
            print('COMMAND.COM      4213 3-27-84')
            print('EDIT.COM         7414 3-27-84')
            time.sleep(3)
            print('FORMAT.COM       5001 3-27-84')
            print('AUTOEXEC.BAT     2006 3-27-84')
            print('CONFIG.SYS       1064 3-27-84')
            print('EDIT.INI          440 3-27-84')
            print('BOOT.MBR          512 3-27-84')
            print('BOOT.BSS          745 3-27-84')
            print('FDISK.EXE        4660 3-27-84')
            print('SDSYS.EXE        3627 3-27-84')
            print("273830 bytes ")
            print("113553 Bytes free")
            time.sleep(5)
            command()
        elif A == 'fdisk.exe':
            print('No fixed disks presents')
            command()
        elif A == 'format.com':
            print("WARNING : ALL DATA ON REMOVABLE DISK A: WILL BE LOST!")
            e = input("DO YOU WISH TO PROCEED?[Y/any invalid option to abort] : ")
            if e == "Y":
                for h in range(41):
                    print('Formatting track ' + str(h))
                    time.sleep(1)
                command()
            else:
                command()
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
                time.sleep(4)
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
                time.sleep(1)
                write = True
                while write == True:
                    print('Please note that this option will wipe any existing file.')
                    d = input('Write anything you want.Type eX1t to quit to DOS.Type c0Mn4mD to exit without save')
                    file += d
                    if d == 'eX1t':
                        write = False
                        file += d
                        command()
                    elif d == 'c0Mn4mD':
                        write = False
                        command
            if C == 3:
                time.sleep(2)
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
            print('REBOOT_INTERNAL : Reboots the machine internally.')
            print('STOP_INTERNAL : Stops the machine internally')
            print('REBOOT : Reboots the host computer')
            print('STOP : Shuts down the host computer.')
            print('NOTE : This version of DOS is a bootdisk and only contains')
            print('minimal commands.To have more commands,eject this disk    ')
            print('and insert an installer disk.Then hold CTRL + ALT and then')
            print('press DEL.You need a Hard drive.Keep this disk as if the  ')
            print('installation fails,you may see what caused it.            ')
            command()
    
        elif A == '':
            command()
        elif A == 'reboot_internal':
            boot()
        elif A == 'stop_internal':
            return
        elif A == 'reboot':
            os.system('shutdown /r /t 0')
        elif A == 'stop':
            os.system('shutdown /s /t 0')
        elif A == 'sdsys.exe':
                print("Sound system now enabled.To test,please do SDSYS.EXE /TEST")
                command()
        elif A == 'sdsys.exe /test':
                print("Sound driver test.")
                print('\a')
                command()
        elif A == 'sdsys.exe /info':
            print("SDSYS Sound System Company")
            print("A compatible card is detected.")
            print("Driver version 2.174")
            print("This card supports EAX,MIDI and SynthWave formats")
            print("Card on slot 4")
            print("Driver enabled at location 00AAFF22CC")
            command()
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
        
boot()
    
            
            
            
