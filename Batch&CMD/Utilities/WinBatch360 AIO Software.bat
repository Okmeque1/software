@echo off
goto start
title WinBatch360 AIO Software
:START
cls
echo WinBatch360 AIO Software 
echo Made by GamerSoftware Corp. and Okmeque1 Computers. (c) All rights reserved.
echo Software360 All-in-1 Software at https://github.com/GamerSoft24/Software/tree/main/BatchSoft/Software360.bat
echo V0.50 beta stage. If action returns to main menu, that means the option is not implemented.
echo [1] UAC Bypass
echo [2] PLACEHOLDER
echo [3] Make Elevated task
echo [4] Start PROGRAM w/flags (e.g : using --user-data-dir and --disable-certificate-errors when starting BrStd1 Browser)
echo [5] Goto CMD.EXE (Non Elevated)
echo [6] Quit
choice /c:123456 /m "Choose an option : "
IF ERRORLEVEL 6 GOTO END
IF ERRORLEVEL 5 GOTO STARTCMD
IF ERRORLEVEL 4 GOTO BRSTD1
IF ERRORLEVEL 3 GOTO SETADMIN
IF ERRORLEVEL 2 GOTO UACBYPASSENCRYPT
IF ERRORLEVEL 1 GOTO UACBYPASS
:UACBYPASS
cls
set /p input="Enter FILE PATH : "
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%input%"
echo.
goto START
:UACBYPASSENCRYPT
cls
REM Gamersoft! You figure out how it works and make the %1 variable to the command on line 17.
echo.
goto START
:SETADMIN
cls
REM See, the CMDLine works using the bypass UAC but the problem is that it opens std cmd prompt and we want admin cmd prompt
echo.
goto START
:BRSTD1
cls
set /p BR="Enter program with or with no parameters. : "
echo %BR%
start "" %BR%
echo.
goto START
:STARTCMD
start
goto END
:END
exit /b
