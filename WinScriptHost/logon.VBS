x = msgbox("Download LOGON2.VBS from the same source for program to function correctly",0+0,"Note")
Set objFSO = CreateObject("Scripting.FileSystemObject")
scriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)
scriptPath = CreateObject("Scripting.FileSystemObject").GetAbsolutePathName(".")
logon2 = objFSO.BuildPath(scriptPath, "logon2.vbs")

Set objShell = CreateObject("Wscript.Shell")

dim password
password = InputBox("Please enter your username (3 attempts left):", "Log on to Windows")

if password = "Okmeque1" then
    MsgBox "Correct username,proceeding...", 64, "Log on to Windows"
    objShell.Run logon2
Else
    dim attemptsLeft
    attemptsLeft = 2
    Do While attemptsLeft >= 0
        password = InputBox("The password you entered is not valid. Please enter your password (" & attemptsLeft & " attempts left):", "Log on to Windows")
        If password = "Okmeque1" Then
            MsgBox "Correct username,proceeding...", 64, "Log on to Windows"
            objShell.Run logon2
            Exit Do
        End If
        attemptsLeft = attemptsLeft - 1
    Loop

    If attemptsLeft = -1 Then
        MsgBox "You have exceeded the maximum number of attempts. The computer will now turn off.", 16, "System message"
        objShell.Run "C:\Windows\system32\shutdown.exe /s /t 5 /c 'Please try again later.'"
    End If
End If
  
