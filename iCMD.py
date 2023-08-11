from tkinter import messagebox
import tkinter as tk
def icmd():
    import os
    iprompt = '>'
    try:
        while True:
            prompt = input(iprompt)
            if prompt == 'exit':
                print("Use 'return' to exit iCMD")
            elif prompt == 'return':
                return False
            os.system(prompt)
    except:
        try:
            print("An exception has occured in function icmd().It may be possible to continue normally.")
            print("Press ENTER <-| to ATTEMPT to continue")
            print("Press CTRL-D/Z to terminate this program")
            input("              Press any key to continue")
            icmd()
        except:
            a = tk.Tk()
            a.withdraw()
            e = messagebox.showwarning("Python","Python has caused an error in\nPYTHON.EXE.\nPython will now close.\n\nIf you continue to experience problems,\ntry restarting your computer.")
            b = messagebox.showerror("PYTHON.EXE - Application error","PYTHON caused a general protection fault in KRNL386.EXE at 0001:8402")
            c = messagebox.showerror("Error","String ERR_NOT_IMPLEMENTED not found in string table.")
            d = messagebox.showerror("","ERR_NOT_IMPLEMENTED")
            exit()

icmd()
        
