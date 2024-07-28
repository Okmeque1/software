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
import html

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

        for F in (MainMenu, OpenWebPage, SendEmail, RandomJoke, SystemCommand, GamesMenu, TicTacToe, TextEditor, ToolsMenu, PassManager, OpenTDB):
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
        l1 = Label(self,text="Text Editor",font=('Arial',18,'bold'))
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
class OpenTDB(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self.l1 = Label(self,text="Points : 0",font=('Arial',14))
        self.l1.pack(pady=5)
        self.l2 = Label(self,text="")
        self.l2.pack(pady=5)
        play = Button(self,text="Play!",command = lambda: self.setup())
        play.pack(pady=5)
        back = Button(self,text="Back to main menu", command=lambda: controller.show_frame(MainMenu))
        back.pack(pady=5)
    def setup(self):
        try:
            x = messagebox.showinfo("G-AIO - Credits","OpenTDB API - By OpenTDB Corp - Licensed under CC BY-SA 4.0. All copies of this program shall mention OpenTDB Corp.")
            numquestion = simpledialog.askinteger("Setup - Question number","Enter number of questions")
            difselect = simpledialog.askstring("Setup - Difficulty Selection","Please select the difficulty by typing the letters in brackets\n[A]ny\n[E]asy\n[M]edium\n[H]ard")
            difmap = {"A":"Any","E":"easy","M":"medium","H":"hard"}
            difselect = difmap[difselect.upper()]
            catselect = simpledialog.askinteger("Setup - Category Selection","""
    0 : Random
    1 : General knowledge
    2 : Books
    3 : Films
    4 : Music
    5 : Music/Teathrals
    6 : Television  
    7 : Video games
    8 : Board games
    9 : Science and nature
    10 : Computer science
    11 : Mathematics science
    12 : Mythology
    13 : Sports
    14 : Geography
    15 : History
    16 : Politics
    17 : Arts
    18 : Celebrities
    19 : Animals
    20 : Vehicles
    21 : Comics
    22 : Gadget science
    23 : Manga/Anime
    24 : Cartoon/Animations
                                                            """) + 8
            typeselect = simpledialog.askstring("G-AIO - Setup Question Type","Please select the question type by typing the letter in brackets.\n[M]ultiple Choice\n[T]rue or False")
            typemap =  {"A":"Any","M":"multiple","T":"boolean"}
            typeselect = typemap[typeselect.upper()]
            questionget = self.geturl(numquestion,difselect,catselect,typeselect)
            automode = messagebox.askyesno("G-AIO - Setup mode","Do you want to enable auto mode?\nAuto mode is a feature where you do not need to select the question, program will do it automatically for you.")
            automap = {True:"Y",False:"N"}
            automode = automap[automode]
            forgivemode = messagebox.askyesno("G-AIO - Setup mode","Do you want to enable forgiveness mode?\nForgiveness mode is a feature where you can redo your failed questions.") if automode == "N" else "N"
            forgivemap = {True:"Y","N":"N",False:"N"}
            forgivemode = forgivemap[forgivemode]
            game = True
            done = []
            pts = 0
            choosequstion = 0
            while game == True:#the actual game. has lots of modes for different things
                self.l1.config(text=f"You have {pts} points.")
                if pts == numquestion:
                    x = messagebox.showinfo("G-AIO - Game Won","You won! Returning to main menu")
                    self.l1.config(text=f"Game Won! You have {pts} points")
                    return
                if automode == "Y":
                    if choosequstion == numquestion:
                        x = messagebox.showerror("G-AIO - Game Lost",f"You lost\nBy a mistake.\nPoints : {pts}")
                        self.l1.config(text="Game Lost!")
                        self.l2.config(text=f"By a mistake.\nPoints : {pts}")
                        return
                    question = html.unescape(str(questionget["results"][choosequstion]["question"]).replace("&quot;","'"))
                    if questionget["results"][choosequstion]["type"] == "multiple":
                        lcorrect = str(questionget["results"][choosequstion]["correct_answer"])
                        l1 = [questionget["results"][choosequstion]["correct_answer"]] + questionget["results"][choosequstion]["incorrect_answers"]
                        random.shuffle(l1)
                        O1 = l1[0]
                        O2 = l1[1]
                        O3 = l1[2]
                        O4 = l1[3]
                        answer = simpledialog.askinteger("G-AIO - Enter answer",f"{question}\nOption 1 : {O1}\nOption 2 : {O2}\nOption 3 : {O3}\nOption 4 : {O4}\nPlease enter the number corresponding to the correct answer.")
                        if l1[answer - 1] == lcorrect:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                            choosequstion += 1
                        else:
                            a = messagebox.showerror("G-AIO - Incorrect Answer","Incorrect answer.")
                            choosequstion += 1
                    else:
                        answer = simpledialog.askstring("G-AIO - Answer Question",f"{question}\n(T)rue/(F)alse? : ")
                        answer = answer.upper()
                        tfmap = {"T":"True","F":"False"}
                        answer = tfmap[answer]
                        if answer == questionget["results"][choosequstion]["correct_answer"]:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            choosequstion += 1
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                        else:
                            a = messagebox.showerror("G-AIO - Incorrect Answer","Incorrect answer.")
                            choosequstion += 1
                else:       
                    
                    choosequstion = simpledialog.askinteger("G-AIO - Select Question","You have selected : " + str(numquestion) + " questions and have to choose. Please choose the question number with the minimum being 1 and the maximum being the number you chose. \nEnter -1 to resign.")
                    if choosequstion == -1:
                        self.l1.config(text="Game lost!")
                        self.l2.config(text=f"By resignation.\nPoints : {pts}")
                        return
                    choosequstion = choosequstion - 1 
                    if questionget["results"][choosequstion] in done:
                        messagebox.showinfo("G-AIO - Completed","You have already completed this question before.")
                    question = str(questionget["results"][choosequstion]["question"]).replace("&quot;","'")
                    if questionget["results"][choosequstion]["type"] == "multiple":
                        lcorrect = str(questionget["results"][choosequstion]["correct_answer"])
                        l1 = [questionget["results"][choosequstion]["correct_answer"]] + questionget["results"][choosequstion]["incorrect_answers"]
                        random.shuffle(l1)
                        O1 = l1[0]
                        O2 = l1[1]
                        O3 = l1[2]
                        O4 = l1[3]
                        answer = simpledialog.askinteger("G-AIO - Enter answer",f"{question}\nOption 1 : {O1}\nOption 2 : {O2}\nOption 3 : {O3}\nOption 4 : {O4}\nPlease enter the number corresponding to the correct answer.")
                        if l1[answer - 1] == lcorrect:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                        else:
                            if forgivemode == "N":
                                done.append(questionget["results"][choosequstion])
                            a = messagebox.showerror("G-AIO - Incorrect Answer","Incorrect answer.")
                    else:
                        answer = simpledialog.askstring("G-AIO - Answer Question",f"{question}\n(T)rue/(F)alse? : ")
                        if answer == questionget["results"][choosequstion]["correct_answer"]:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                        else:
                            if forgivemode == "N":
                                done.append(questionget["results"][choosequstion])
                            a = messagebox.showerror("G-AIO - Incorrect Answer","Incorrect answer.")         
        except Exception as e:
            x = messagebox.showerror("G-AIO - Setup OpenTDB",f"Game or Setup failed. Error {e}")
    def geturl(self,amount=1,difficulty="easy",category=9,typee="multiple"):#geturl function calls opentdb.com and returns what it responds in JSON
        returnstring = "https://opentdb.com/api.php"
        returnstring += "?amount=" + str(amount)
        returnstring += "&category=" + str(category)
        returnstring += "&difficulty=" + difficulty
        returnstring += "&type=" + typee
        print(returnstring)
        returnurl = requests.get(returnstring)
        return html.unescape(returnurl.json())

class GamesMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Games Menu.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        tic_tac_toe_button = tk.Button(self, text="Tic-Tac-Toe.", command=self.play_tic_tac_toe)
        tic_tac_toe_button.pack(pady=5)
        opentdb = Button(self,text="Open Trivia Questions",command=lambda: controller.show_frame(OpenTDB))
        opentdb.pack(pady=5)
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
        label = tk.Label(self, text="Tools Menu", font=('Arial', 18, 'bold'))
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
        label = tk.Label(self, text="Password Manager", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)   
        b1 = Button(self,text="Generate password",command=lambda: self.gen(""))
        b1.pack(pady=5)
        b2 = Button(self,text="Retrieve password",command=lambda: self.retrieve())
        b2.pack(pady=5)
        b3 = Button(self,text="List passwords",command=lambda: self.showall())
        b3.pack(pady=5)
        b4 = Button(self,text="Back to Main Menu",command=lambda: controller.show_frame(MainMenu))
        b4.pack(pady=5)
        self.t1 = Text(self,width=80,height=16)
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
