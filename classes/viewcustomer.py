from tkinter import Tk
from tkinter import *
from tkinter import messagebox
import pymysql


class View:
    """ View
            This class is declared for vieweing the details of customer
    """

    def __init__(self):
        mainwindow = Tk()
        mainwindow.config(background="#e0e0e0")
        self.wn = mainwindow
        self.wn.geometry('480x200+500+300')
        self.wn.title("Show Customer")
        self.wn.resizable(False, False)
        self.customer_details = []
        self.my_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="coffeemanagementsystem"
        )
        sql = "select * from customer_details"
        self.my_cursor = self.my_connection.cursor()
        self.my_cursor.execute(sql)
        results = self.my_cursor.fetchall()
        # print(results)
        for i in results:
            # print(i)
            self.customer_details.append(i)

        # print(self.customer_details)
        self.allcustomers_window()
        self.wn.mainloop()

    def allcustomers_window(self):
        self.search_id = StringVar(self.wn)
        Label(self.wn, text="Enter Customer ID", font=("Times New Roman", 16), bg="#e0e0e0").place(x=30, y=49)
        Entry(self.wn, text="Enter ID", textvariable=self.search_id, font=("Times New Roman", 16), width=24).place(x=28,
                                                                                                                   y=100)
        Button(self.wn, text="Search", font=("Times New Roman", 16, "underline"), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", command=self.search_customer, width=10).place(x=300, y=92)

    def search_customer(self):
        print("in customer details")
        # print(self.customer_details)
        i = 0
        for customer in self.customer_details:
            if str(self.search_id.get()) == str(customer[0]):
                self.create_new_win(customer)
                exit(0)
            else:
                i += 1
        else:
            messagebox.showerror("ERROR", "No such customer on the database.")

    def create_new_win(self, customer):
        new = Tk()
        new.title("Customer Details")
        new.geometry('600x350')
        new.config(background="#dabc98")

        main_title = Label(new, text="Details About Customer", font=("Times New Roman", 16, "underline"),
                           bg="#d19063",
                           fg="white",
                           activeforeground="white"
                           , width="46",
                           height="2").place(x=18, y=20)

        details_line = ['Customer ID', 'Name', 'Email', 'Contact']
        y = 100
        count = 0
        for details in customer:
            Label(new, text=details_line[count], font=("Times New Roman", 16), bg="#735039", fg="white",
                  activebackground="#735039",
                  activeforeground="white",
                  state=ACTIVE, width=15).place(x=40, y=y)
            Label(new, text=":", font=("Times New Roman", 16), bg="#735039", fg="white",
                  activebackground="#735039",
                  activeforeground="white",
                  state=ACTIVE).place(x=200, y=y)
            Label(new, text=details, font=("Times New Roman", 16), bg="#dabc98").place(x=250, y=y)
            y += 55
            count += 1

        new.mainloop()



