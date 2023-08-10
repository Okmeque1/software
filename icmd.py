from tkinter import messagebox
import tkinter as tk
def icmd():
    import os
    try:
        while True:
            prompt = input(">")
            os.system(prompt)
    except:
        try:
            print("An exception has occured in function icmd().It may be possible to continue normally.")
            print("Press ENTER <-| to ATTEMPT to continue")
            print("Press CTRL-C/D/Z to terminate the program")
            input("              Press any key to continue")
        except:
            a = tk.Tk()
            a.withdraw()
            e = messagebox.showwarning("Python","Python has caused an error in\nPYTHON.EXE.\nPython will now close.\n\nIf you continue to experience problems,\ntry restarting your computer.")
            b = messagebox.showerror("PYTHON.EXE - Application error","PYTHON caused a general protection fault in KRNL386.EXE at 0001:8402")
            c = messagebox.showerror("Error","String ERR_NOT_IMPLEMENTED not found in string table.")
            d = messagebox.showerror("","ERR_NOT_IMPLEMENTED")
            exit()

icmd()
        