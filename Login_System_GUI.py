from tkinter import *
from tkinter import messagebox
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

class BATE:
    def __init__(self):
        self.users = {}
    
    def create_account(self):
        username = self.Username_bar.get()
        password = self.Password_bar.get()
        user = User(username, password)
        self.users[username] = user
        messagebox.showinfo("Success", "Account created successfully!")
    
    def log_in(self):
        username = self.Username_bar.get()
        password = self.Password_bar.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in self.users and self.users[username].password == hashed_password:
            messagebox.showinfo("Success", "Logged in successfully!")
        else:
            messagebox.showerror("Error", "Invalid username or password")


    def open1(self):
        self.top = Toplevel()
        self.top.geometry("300x200")
        self.top.title("B.A.T.E Internet")
        self.frame = LabelFrame(self.top, padx=10, pady=10)
        self.frame.pack(padx=10, pady=3)

        self.Title = Label(self.frame, text="---ACCOUNT CREATION MENU---", font=("Bodoni",13,"bold"))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.objective = Label(self.frame, text="Please enter information to create an account!")
        self.objective.grid(row=1, column=0, columnspan=2)

        self.Username = Label(self.frame, text="Username", font="Bodoni")
        self.Username.grid(row=2, column=0)
        self.Username_bar = Entry(self.frame, width=27, borderwidth=3)
        self.Username_bar.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

        self.Password = Label(self.frame, text="Password", font="Bodoni")
        self.Password.grid(row=3, column=0)
        self.Password_bar = Entry(self.frame, width=27, borderwidth=3, show="*")
        self.Password_bar.grid(row=3, column=1, columnspan=2, padx=3, pady=3)

        self.create_button = Button(self.top, text="Create account", font=("Bodoni",12,"bold"), command=self.create_account)
        self.create_button.pack()

        self.exit_button = Button(self.top, text="Return", command=self.top.destroy)
        self.exit_button.pack()
    
    def open2(self):
        self.top = Toplevel()
        self.top.geometry("300x200")
        self.top.title("B.A.T.E Internet")
        self.frame = LabelFrame(self.top, padx=10, pady=10)
        self.frame.pack(padx=10, pady=3)

        self.Title = Label(self.frame, text="---ACCOUNT LOGIN MENU---", font=("Bodoni",13,"bold"))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.objective = Label(self.frame, text="Please enter information to login!")
        self.objective.grid(row=1, column=0, columnspan=3)

        self.Username = Label(self.frame, text="Username", font="Bodoni")
        self.Username.grid(row=2, column=0)
        self.Username_bar = Entry(self.frame, width=27, borderwidth=3)
        self.Username_bar.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

        self.Password = Label(self.frame, text="Password", font="Bodoni")
        self.Password.grid(row=3, column=0)
        self.Password_bar = Entry(self.frame, width=27, borderwidth=3, show="*")
        self.Password_bar.grid(row=3, column=1, columnspan=2, padx=3, pady=3)

        self.login_button = Button(self.top, text="Login", font=("Bodoni",12,"bold"), command=self.log_in)
        self.login_button.pack()

        self.exit_button = Button(self.top, text="Return", command=self.top.destroy)
        self.exit_button.pack()


    def run(self):
        self.root = Tk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("300x166")

        self.frame = LabelFrame(self.root, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        self.Title1 = Label(self.frame, text="---WELCOME TO B.A.T.E---", font=("Bodoni",14,"bold"))
        self.Title1.grid(row=0, column=0, columnspan=3)

        self.SubTitle1 = Label(self.frame, text="Welcome customer! Please select your action!")
        self.SubTitle1.grid(row=1, column=0, columnspan=2)

        self.Create_Acc_Menu = Button(self.frame, text="Register", font=("Bodoni",12,"bold"), pady=5, command=self.open1)
        self.Create_Acc_Menu.grid(row=2, column=0)

        self.Login_Menu = Button(self.frame, text="Login", font=("Bodoni",12,"bold"), pady=5, command=self.open2)
        self.Login_Menu.grid(row=2, column=1)

        self.button = Button(self.root, text="Exit", command=self.root.quit).pack()

        self.root.mainloop()

bate = BATE()
bate.run()