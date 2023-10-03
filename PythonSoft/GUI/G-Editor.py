import tkinter as tk
from tkinter import *
from tkinter import messagebox
def load(filename):
    text.delete("1.0",END)
    try:
        with open(filename,"r") as returnname:
            a = returnname.read()
            text.insert(END,a)
            return
    except FileNotFoundError:
        filenotfound = messagebox.showerror("Error","Load failed.Make sure that the file exists and try again.\nError code : 6510B")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Load failed.Make sure that you have the proper permissions and try again\nError code : 0210")
           return
    except BaseException:
        baseexec = messagebox.showerror("Error","Load failed.Check the file and permissions and try again.\nError code : 770A")
        return
def save(text,filename):
    try:
        with open(filename,"w") as writing:
            writing.write(text)
            success = messagebox.showinfo("G-Editor","Save complete!")
            return
    except FileExistsError:
        fileexist = messagebox.showerror("Error","Save failed.Choose a different file name and try again\nError code : 6510A")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Save failed.Make sure that you have the proper permissions and try again\nError code : 0210")
           return    
    except BaseException:
         baseexec = messagebox.showerror("Error","Save failed.Check file names,permissions and disk space and try again.\nError code : 770A")
         return
def about():
    abou = messagebox.showinfo("G-Editor - About","About this program\nWritten by Okmeque1 starting Thu 28/09/2023 finishing Sat 09/30/2023 15:41\nThis program is run by tkinter and is open-source.You may copy it onto any form of media whether it be a : \n-USB,CD or DVD\n-Cloud storage(NAS or Google drive)\n-Or on Github...\nso long you mention Okmeque1 in the code.\n\nThe save button can save or create a file,so long the file isn't obstructing with any present files.When loading,make sure the file exists.")
windows = Tk()
windows.geometry("800x600")
windows.title("G-Editor")
windows.resizable(width=False, height=False)
loop = True
text = Text(windows,height=29.71,width=100)
file_name = None
while loop == True:
    l1 = Label(windows,text="File name : ")
    ldl = Entry(windows,width=40)
    ld = Button(windows,text="Load",command = lambda: load(ldl.get()),width=40,activebackground="gray")
    sv = Button(windows,text="Save",command = lambda: save(text.get("1.0",END),ldl.get()),width=40,activebackground="gray")
    ab = Button(windows,text="About",command = about,width = 40,activebackground="gray")
    text.pack()
    l1.pack()
    ldl.pack()
    ld.pack()
    sv.pack()
    ab.pack()
    windows.mainloop()
