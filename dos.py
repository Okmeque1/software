from os import system

print('MS-DOS Version 3.30')
print('Hard Disk or and 2nd floppy not detected')
def command():
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
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('#########################################')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
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

        
        
        