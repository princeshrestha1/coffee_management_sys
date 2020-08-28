from tkinter import *
import os
from tkinter import messagebox as m_box
import Home_dashboard




class Login:
    def login(self):
        global loginwin
        global username
        global password

        global username_verify
        global pwd_verify

        username_verify = StringVar()
        pwd_verify = StringVar()

        global e1
        global e2

        loginwin = Toplevel(mainwindow)
        loginwin.geometry("549x470")
        loginwin.title("Coffee Management System")
        loginwin.resizable(False, False)
        loginwin.config(background="#e0e0e0")
        main_title = Label(loginwin, text="Login", font=("Times New Roman", 16, "underline"), bg="#d19063",
                           fg="white", width="500",
                           height="3")
        main_title.pack()

        username_label = Label(loginwin, text="Username", bg="#e0e0e0")
        username_label.place(x=244, y=160)
        username_verify = StringVar()
        e1 = Entry(loginwin, textvariable=username_verify, width="40")
        e1.place(x=155, y=185)
        pwd_verify = StringVar()
        password_label = Label(loginwin, text="Password", bg="#e0e0e0")
        password_label.place(x=245, y=210)

        e2 = Entry(loginwin, show="*", textvariable=pwd_verify, width="40")
        e2.place(x=155, y=235)
        verifyy = Button(loginwin, text="Verify", width="25", height="2", bg="#735039", fg="white",
                         activebackground="#735039", activeforeground="white",
                         state=ACTIVE, command=loginverification)
        verifyy.place(x=185, y=305)
        #
        # add = Button(loginwin, text="Add", width="25", height="2", bg="#e6e6e6", fg="#4169E1", activebackground="#4169E1",
        #              activeforeground="white",
        #              state=ACTIVE, command=employee_reg)
        # add.place(x=195, y=365)

        loginwin.mainloop()


l1= Login()



def loginverification():
    username = username_verify.get()
    password = pwd_verify.get()
    e1.delete(0, END)
    e2.delete(0, END)

    if username == 'admin' and password == 'admin':
        loginissucess()

    elif password != 'admin':
        wrongpassword()

    else:
        print("user not found")
        usernotregistered()



def loginissucess():
    global loginsuccesswin
    loginsuccesswin = Toplevel(loginwin)
    loginsuccesswin.title("Success")
    loginsuccesswin.geometry("150x100")
    Label(loginsuccesswin, text="Login is Successful").pack()
    Button(loginsuccesswin, text="OK", command=move_to_home).pack()

def move_to_home():
    mainwindow.destroy()
    k = Tk()
    home = Home_dashboard.Home(k)
    k.mainloop()


def wrongpassword():
    global wrongpasscodewin
    wrongpasscodewin = Toplevel(loginwin)
    wrongpasscodewin.title("Success")
    wrongpasscodewin.geometry("150x100")
    Label(wrongpasscodewin, text="Invalid Password ").pack()
    Button(wrongpasscodewin, text="OK", command=deletewrongpassword).pack()

def usernotregistered():
    global usernotregstrdwin
    usernotregstrdwin = Toplevel(loginwin)
    usernotregstrdwin.title("usernotregistrdSuccess")
    usernotregstrdwin.geometry("150x100")
    Label(usernotregstrdwin, text="User Not Found").pack()
    Button(usernotregstrdwin, text="OK", command=deleteusernotregistrd).pack()



def deleteloginissuccess():
    loginsuccesswin.destroy()


def deletewrongpassword():
    wrongpasscodewin.destroy()


def deleteusernotregistrd():
    usernotregstrdwin.destroy()






def usermanagescreen():
    global mainwindow
    mainwindow = Tk()
    mainwindow.geometry("870x520+1+1")
    mainwindow.title("Coffee Management System")
    mainwindow.resizable(False, False)
    mainwindow.config(background="#e0e0e0")

    f1 = Frame(mainwindow, bd=9, relief=RIDGE, bg="#e0e0e0")
    f1.place(x=132, y=100, height=295, width=600)

    main_title = Label(f1,text="Welcome To admin page", font=("Times New Roman", 16, "underline"), bg="#d19063", fg="white",
                       height="2", width="48").grid(row=0, column=2, pady=24)
    loginbutton = Button(f1, text="LOGIN", height=3, width=30, bg="#735039", fg="white",bd=5,
                         activebackground="#735039", activeforeground="white",
                         state=ACTIVE, command=l1.login)
    loginbutton.place(x=187, y=155)

    mainwindow.mainloop()


usermanagescreen()









































