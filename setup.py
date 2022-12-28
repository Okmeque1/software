import time







def setup():
    print('========================================')
    print('             Windows 98 setup           ')
    print('========================================')
    print('A : Install Windows from CD')
    print('B : Start computer with CDROM support   ')
    print('C : Start computer in plain DOS shell.  ')
    setup_input = input('Pick a choice : A (A) , B (B) , C (C) ')
    if setup_input == 'A':
        print('Microsoft ScanDisk.')
        scandisk = input ('Scandisk is checking sectors in drive C.Press ENTER to continue')
        if scandisk == '':
            print('Checking sector 0')
            time.sleep(5)

        copy = input('Setup will now copy all of the required files.Press ENTER to continue')
        if copy == '':
            print('Setup will now continue')
        for y in range(100001):
            print('Setup is copying file number')
            print(y)
            print('File successfully copied to drive C')
        print('Setup needs to restart your computer to continue.')
        file = input('Your computer will restart when you press ENTER')
        if file == '':
            print('Your computer should restart')
        print('===============================================')
        print('GeForce FX 5150 Pro BIOS N34.EP.08')
        print('Version 4.34.20.87.0P')
        print('Copyright (C) 1996-2003 NVIDIA Corp')
        print('128.560MB RAM')
        print('Pentium III : 900Mhz   (AMIBIOS VERSION 8.1)   ')
        print('160384 OK')
        print('Please enter your product key(e.g : XXXXX-XXXXX-XXXXX-XXXXX-XXXXX)Press ` to abort setup')
        product_key = input('')
        if product_key == 'ZF3R0-FHED2-M80TY-8QYGC-NPKYF':
            print('Setup will now continue')
        if product_key == '`':
            return
        else:
            print('Invalid product key.Please try again')
            product_key
        print('Setup is now scanning for plug and play hardware')
        print('If your computer is not responding,restart your computer')
        for g in range(201):
            print('Updating system setting')
            print(g)
        print('Setup has finished configuring your system.Please reboot')
    if setup_input == 'B':
        print('Computer is loading MSCDEX.EXE,please wait')
        print('CD driver installed.CDROM drive is now mounted as D:')
        print('MSCDEX version 2.25')
    if setup_input == 'C':
        print('Loading virtual floppy drive mounter(FLPMOUNT.EXE)')
        print('Virtual floppy drive is now B:.Any phisical floppy drives are A:')
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
    if A == 'fdisk.exe':
        print('No fixed disks presents')
        command()
    if A == 'format.com':
        for h in range(41):
            print('Formatting track')
            print(h)
    if A == 'autoexec.bat':
        command()
    if A == 'command.com':
        command()
    if A == 'edit.com':
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
    if A == 'xcopy.exe':
        print('No other drives or disks have been detected.This includes hard drives,or other floppy disks')
        command()
    if A == 'copy':
        print('Sorry,this disk is write-protected.')
    if A == 'ver':
        print('MS-DOS 3.30')
    if A == 'Okmeque1':
        print('Okmeque1 DOS version 1.12 running on 360K A: drive.')
    if A == 'specs':
        print('4.77/8 Mhz IBM AT.630K RAM.')
    if A == 'help':
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

    if A == '':
        command()
    if A == 'stop':
        return        
    else:
        print('Bad command or file name')
        command()   
    

def mscdex():
    print('CD driver installed.CDROM drive is now mounted as D:')
    print('MSCDEX version 2.25')
def FLPMOUNT():
    print('Loading virtual floppy drive mounter(FLPMOUNT.EXE)')
    print('Virtual floppy drive is now B:.Any phisical floppy drives are A:')
def fdisk():
    print('A : Partition drive C')
    print('B : delete Non-DOS partition')
    print('C : Exit program.')
    fdisk_input = input('Pick a choice : A (A) ,B (B) , C (C)') 
    if fdisk_input == 'A':
        for f in range(7531):
            print('Partitioning sector')
            print(f)
        print('System will now restart') 
        kickstart()
    if fdisk_input == 'B':
        print('Non DOS partition deleted')
        fdisk()
    if fdisk_input == 'C':
        print('Exiting FDISK')
def format():
    for h in range(7531):
        print('Formatting sector')
        print(h)

def winkey():
    return 'ZF3R0-FHED2-M80TY-8QYGC-NPKYF'
def win():
    print('==============================================')
    print('             Windows 98 startup menu          ')
    print('==============================================')
    print('A : Normal boot')
    print('B : Safe mode')
    print('C : command prompt only')
    win_opt = input('Pick a choice : A (A), B (B),C (C)')
    if win_opt == 'A':
        setup()
    if win_opt == 'B':
        for r in range(3001):
            print('Loading file number')
            print(r)
    if win_opt == 'C':
        print('Windows 98[4.10.2222A]')
        command()
def ver():
    return 'Windows 98[4.10.2222A]'
def utilities():
    print('There is fdisk,mscdex,winkey,win,setup,ver and flpmout,etc.')
    print('All of which have different utilities.')
    print('To execute a program,type in the commandline : Program()')    
    print('NOTE : The program to demonstrate how to execute it can be a program')
    print('from the list above')
def power():
    print('A : Shutdown,B : Reboot, C : Abort this program')
    power_input = input('A,B or C?')
    if power_input == 'A':
        return 'This machine is now OFF'
    if power_input == 'B':
        print('Rebooting now')
        kickstart()
    if power_input == 'C':
        return 'Program terminated.'
    
    

 

def kickstart():
    print('===============================================')
    print('GeForce FX 5150 Pro BIOS N34.EP.08')
    print('Version 4.34.20.87.0P')
    print('Copyright (C) 1996-2003 NVIDIA Corp')
    print('128.560MB RAM')
    print('This card is running on the PCIE slot.')
    print('Pentium III : 900Mhz   (AMIBIOS VERSION 8.1)   ')
    print('160384 OK')
    print('WARNING : ISA Bus is not working normally.Disabling device until it functions.Possible reasons are no drivers')
    print('Hit DEL for BIOS')
    print('Hit F12 for boot device')
    print('Detected on IDE : 0 is ST1000LM035-1RK172 1000.2 GB')
    print('Detected on IDE : 1 is DVDROMRW50021521')
    print('Floppy drive : SONY FLP35144MB')
    print('Front panel ports are : 2X USB3.0, 1X FIREWIRE800, 2X HEADPHONE_JACK')
    print('Starting Windows...')
    for g in range(101):
        print('Checking file...File not corrupt or missing,loading file')
    print('Windows has detected that the ISA bus is not functioning correctly')
    print('Windows failed to start.Returning to command prompt')
    print('Error code :  671F5C2BFB6A46C09161924FCC9826B9DB3EDGE1916')
    winerr = input('Do you want to try again?[Y,N]')
    if winerr == 'Y':
        print('===============================================')
        print('GeForce FX 5150 Pro BIOS N34.EP.08')
        print('Version 4.34.20.87.0P')
        print('Copyright (C) 1996-2003 NVIDIA Corp')
        print('128.560MB RAM')
        print('This card is running on the PCIE slot.')
        print('Pentium III : 900Mhz   (AMIBIOS VERSION 8.1)   ')
        print('160384 OK')
        print('WARNING : ISA Bus is not working normally.Disabling device until it functions.Possible reasons are no drivers')
        print('Hit DEL for BIOS')
        print('Hit F12 for boot device')
        print('Detected on IDE : 0 is ST1000LM035-1RK172 1000.2 GB')
        print('Detected on IDE : 1 is DVDROMRW50021521')
        print('Floppy drive : SONY FLP35144MB')
        print('Front panel ports are : 2X USB3.0, 1X FIREWIRE800, 2X HEADPHONE_JACK')
        print('Starting Windows...')
        win()
    if winerr == 'N':
        print( 'Aborted.')
kickstart()

def isa_driver():
    driver01 = input('This will install the ISA drivers for this system(Amiga 7000)[Y,N]')
    if driver01 == 'Y':
        for k in range(7451):
            print('Copying file number')
            print(k)
        print('Configuring drivers...done')
        print('Please restart your computer')
        power()
def fx5150pro_drivers():
    driver02 = input('This will install the FX 5150 Pro drivers(WIN95/98/ME) for this system(Amiga 7000)[Y,N]')
    if driver02 == 'Y':
        for k in range(7451):
            print('Copying file number')
            print(k)
        print('Configuring drivers...done')
        print('Please restart your computer')
        power()
def load():
    print('Loading MS.PACMAN,ETA 12 SEC')
    

            
            

            

            

            


    























    



















    