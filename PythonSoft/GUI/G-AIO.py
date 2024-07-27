import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import *
import datetime     
import requests
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import random
import os
import json

class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033{4m'
    END = '\033[0m'

class AssistantApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("G-AIO")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, OpenWebPage, SendEmail, RandomJoke, SystemCommand, GamesMenu, TicTacToe, TextEditor, ToolsMenu, PassManager):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Main Menu.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        options = [
            ("Open a Web Page.", lambda: controller.show_frame(OpenWebPage)),
            ("Send an Email.", lambda: controller.show_frame(SendEmail)),
            ("Fetch a Random Joke.", lambda: controller.show_frame(RandomJoke)),
            ("Execute a System Command.", lambda: controller.show_frame(SystemCommand)),
            ("Games Menu.", lambda: controller.show_frame(GamesMenu)),
            ("Text Editor", lambda: controller.show_frame(TextEditor)),
            ("Tools Menu", lambda: controller.show_frame(ToolsMenu)),
            ("Exit.", self.quit)
        ]

        for text, command in options:
            button = tk.Button(self, text=text, width=40, height=2, command=command)
            button.pack(pady=5)
    def gettime(self):
        return datetime.datetime.now()
class OpenWebPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        l1 = Label(self,text="Browser Location (leave blank for default browser)")
        l1.pack(pady=5)
        self.other_BR = Entry(self,width=100)
        self.other_BR.pack(pady=5)
        l2 = Label(self,text="URL")
        l2.pack(pady=5)
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=10, padx=10)

        open_button = tk.Button(self, text="Open.", command=self.open_webpage)
        open_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def open_webpage(self):
        
        if self.other_BR.get() == "":
            url = self.url_entry.get()
            webbrowser.open(url)
        else:
            try:
                result = subprocess.run(f'start "" {self.other_BR.get()} {self.url_entry.get()}', shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    pass
                else:
                    messagebox.showerror("G-AIO",f"Failed to start browser. Error: {result.stderr}")
            except Exception as e:
                messagebox.showerror("G-AIO", f"Failed to start browser. Error: {str(e)}.")            

class SendEmail(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Send an Email.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.to_label = tk.Label(self, text="To:.")
        self.to_label.pack()

        self.to_entry = tk.Entry(self, width=50)
        self.to_entry.pack(pady=5)

        self.subject_label = tk.Label(self, text="Subject:.")
        self.subject_label.pack()

        self.subject_entry = tk.Entry(self, width=50)
        self.subject_entry.pack(pady=5)

        self.message_label = tk.Label(self, text="Message:.")
        self.message_label.pack()

        self.message_text = tk.Text(self, width=50, height=10)
        self.message_text.pack(pady=5)

        send_button = tk.Button(self, text="Send.", command=self.send_email)
        send_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def send_email(self):
        smpt = simpledialog.askstring("SMTP Server","Enter an SMTP server for your mail provider. Default is 'smtp.gmail.com'\nIf you do not spell it correctly, you will get an error!")
        port = simpledialog.askinteger("SMTP Server Port","Enter a port for your SMTP server. Default for GMail is 587")
        mail = simpledialog.askstring("Email address","Enter an email address that corresponds to your provider. This will affect how the password works.")
        pwd = simpledialog.askstring("Password","Enter an app or regular passwords. GMail requires app passwords due to security restrictions, which can be found at https://myaccount.google.com/apppasswords.\nIf with another email provider, check for more info.")
        to_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        from_email = mail # Replace with your email address (Gmail only. You can change the SMTP server and port below for other mail providers.)
        app_pwd_or_std_pwd = pwd # Replace with you Gmail App Password. Regular password will not work due to Gmail Security Restrictions. If you want to use an other mail provider, check their security restrictions to see if you need an App Password like Gmail or not.

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP(smpt, port) # You can change the SMTP server and port here if you want a different mail provider like Outlook or Yahoo. Search online for more information.
            server.starttls()
            server.login(from_email, app_pwd_or_std_pwd)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            messagebox.showinfo("Email.", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Email.", f"Failed to send email. Error: {str(e)}.")

        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)

class RandomJoke(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Random Joke.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.joke_label = tk.Label(self, text="", font=('Arial', 14))
        self.joke_label.pack(pady=10)

        fetch_button = tk.Button(self, text="Fetch Joke.", command=self.fetch_joke)
        fetch_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def fetch_joke(self):
        try:
            response = requests.get('https://official-joke-api.appspot.com/random_joke')
            if response.status_code == 200:
                joke = response.json()
                self.joke_label.config(text=f"{joke['setup']}\n{joke['punchline']}.")
            else:
                messagebox.showerror("Joke.", "Failed to fetch joke from API, check firewall and internet restrictions.")
        except Exception as e:
            messagebox.showerror("Joke.", f"Failed to fetch joke. Error: {str(e)}.")

class SystemCommand(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="System Command.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.command_entry = tk.Entry(self, width=50)
        self.command_entry.pack(pady=10)

        execute_button = tk.Button(self, text="Execute.", command=self.execute_command)
        execute_button.pack(pady=5)

        self.output_text = tk.Text(self, width=80, height=18)
        self.output_text.pack(pady=10)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def execute_command(self):
        command = self.command_entry.get()
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Command executed successfully.\nOutput:\n{result.stdout}.")
            else:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Command failed with error:\n{result.stderr}.")
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Failed to execute command. Error: {str(e)}.")
class TextEditor(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        l1 = Label(self,text="Text Editor - By Okmeque1",font=('Arial',18,'bold'))
        l1.pack(pady=10,padx=10)
        self.text = Text(self,width=80,height=20)
        self.text.pack(pady=10)
        l2 = Label(self,text="File Name")
        l2.pack(pady=5)
        self.filename = Entry(self,width=40)
        self.filename.pack(pady=10)
        load = Button(self,text="Load",command=lambda: self.load(),width=40)
        load.pack(pady=5)
        save = Button(self,text="Save",command=lambda: self.save(),width=40)
        save.pack(pady=5)
        menu = Button(self,text="Return to Main Menu",command=lambda: controller.show_frame(MainMenu),width=40)
        menu.pack()
    def load(self):
        try:
            with open(self.filename.get(),"r") as reading:
                self.text.delete("1.0",END)
                self.text.insert(END,reading.read())
        except Exception as e:
            x = messagebox.showerror("G-AIO - Load failed",f"Load failed. Error : {str(e)}")
    def save(self):
        try:
            with open(self.filename.get(), "w") as writing:
                writing.write(self.text.get("1.0",END))
                x = messagebox.showinfo("G-AIO","Save complete.")
        except Exception as e:
            x = messagebox.showerror("G-AIO - Save failed",f"Save failed. Error : {str(e)}")
            
class GamesMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Games Menu.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        tic_tac_toe_button = tk.Button(self, text="Tic-Tac-Toe.", command=self.play_tic_tac_toe)
        tic_tac_toe_button.pack(pady=5)

        flappy_bird_button = tk.Button(self, text="Flappy Bird (Coming Soon).", state=tk.DISABLED)
        flappy_bird_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def play_tic_tac_toe(self):
        self.controller.show_frame(TicTacToe)

class TicTacToe(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        label = tk.Label(self, text="Tic-Tac-Toe.", font=('Arial', 18, 'bold'))
        label.pack(pady=10)

        self.buttons = []
        for i in range(3):
            row_frame = tk.Frame(self)
            row_frame.pack()
            for j in range(3):
                button = tk.Button(row_frame, text=" ", font=('Arial', 20, 'bold'), width=8, height=4,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.pack(side="left", padx=5, pady=5)
                self.buttons.append(button)

        #reset_button = tk.Button(self, text="Reset.", command=self.reset_game)
        #reset_button.pack(pady=10)

        back_button = tk.Button(self, text="Back to Games Menu.", command=lambda: controller.show_frame(GamesMenu))
        back_button.pack(pady=10)

    def click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe.", f"{self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic-Tac-Toe.", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"
class ToolsMenu(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Tools Menu - By Okmeque1", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)   
        pwd = Button(self, text="Password Manager", command=lambda: controller.show_frame(PassManager))
        pwd.pack(pady=5)
        smsr = Button(self, text="Remove Start Menu Search Results",command=lambda: self.start())#Windows Only, removes bing search results     
        smsr.pack(pady=5)
        back = Button(self,text="Back to main menu", command=lambda: controller.show_frame(MainMenu))
        back.pack(pady=5) #it's a backpack!
    def start(self):
        if os.name != 'nt':
            x = messagebox.showwarning("G-AIO","The 'Windows Start Menu Internet Search Results Remover' is not compatible with your operating system.")
            return
        a = os.system("reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer\DisableSearchBoxSuggestions /d 1")
        if a != 0:
            x = messagebox.showerror("G-AIO","Please run this program with admin privileges for this function to work properly.")
        else:
            x = messagebox.askyesno("G-AIO","The operation has completed successfully. For the changes to take effect, the Windows Explorer must be restarted and will take a few moments. Restart?",icon=messagebox.QUESTION)
            if x:
                os.system('taskkill /f /im explorer.exe')
                os.system('explorer')
class PassManager(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)   
        self.controller = controller
        label = tk.Label(self, text="Password Manager - By Okmeque1", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)   
        b1 = Button(self,text="Generate password",command=lambda: self.gen(""))
        b1.pack(pady=5)
        b2 = Button(self,text="Retrieve password",command=lambda: self.retrieve())
        b2.pack(pady=5)
        b3 = Button(self,text="List passwords",command=lambda: self.showall())
        b3.pack(pady=5)
        self.t1 = Text(self,width=80,height=18)
        self.t1.pack(pady=10)
    def gen(self,setname1):
        charlen = simpledialog.askinteger("G-AIO","Enter password length")
        print(setname1)
        if setname1 == "": #originally I put != "" because... well idk really, just brainrot moment.
            setname = simpledialog.askstring("G-AIO","Enter password name")
        else:
            setname = setname1

        charset = '¦¬`1!23£4$€5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
        pwd = ""
        for x in range(charlen):
            pwd += random.choice(charset)
        filename = simpledialog.askstring("G-AIO","Please enter a valid file name. The format must be 'A:\Directory\Subdirectory\file.extension'.")
        try:
            with open(filename,"a") as add:
                add.write(f"\n{setname} -> {pwd}")
                x = messagebox.showinfo("G-AIO","Generated and saved successfully")
        except Exception as e:
            x = messagebox.showerror("G-AIO - Save failed",f"Save failed. Error : {e}")
    def retrieve(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            with open(filename,"r") as passopen:
                set1 = simpledialog.askstring("G-AIO","Enter password name")
                success = False
                for line in passopen:
                    if line.split(" -> ")[0] == set1:
                        success = True
                        x = messagebox.showinfo("G-AIO","The password is " + str({line.split(" -> ")[1]}))   
                        self.t1.delete("1.0",END)
                        self.t1.insert(END,"The password for the password name is ")
                        self.t1.insert(END,line.split(" -> ")[1])
                        return
                if success != True:
                    gotogen = messagebox.askquestion("G-AIO",f"The password '{set1}' does not exist. \nWould you like to create it?")
                    if gotogen == 'yes':
                        self.gen(set1)
                    else:
                        gotogen = messagebox.showerror("G-AIO","The password could not be loaded.\nThe requested password was not found.")
    def showall(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            with open(filename,"r") as listall:
                self.t1.delete("1.0",END)
                self.t1.insert(END,"The passwords for this file are :\n")
                self.t1.insert(END,listall.read())
if __name__ == "__main__":#uarte
    app = AssistantApp()
    app.geometry("800x600")
    app.mainloop()
