from tkinter import Tk
from tkinter import *
from tkinter import messagebox


class View:
    """ View
            This class is declared for vieweing the details of customer
    """
    def __init__(self, window):
        self.wn = window
        self.wn.geometry('480x200+500+300')
        self.wn.title("Show Customer")
        self.wn.resizable(False, False)
        self.customer_details = []
        with open("C:\\Users\\User\\PycharmProjects\\CoffeeShopManagementSystem\\classes\\customer_details.txt") as show_customer:
            for lines in show_customer:
                self.customer_details.append(lines.split(","))
        self.allcustomers_window()

    def allcustomers_window(self):
        self.search_id = StringVar(self.wn)
        Label(self.wn, text="Enter Customer ID", font=("Times New Roman", 16)).place(x=30, y=49)
        Entry(self.wn, text="Enter ID", textvariable=self.search_id, font=("Times New Roman", 16),width=24).place(x=28, y=100)
        Button(self.wn, text="Search", font=("Times New Roman", 16, "underline"),  bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", command = self.search_employee,width=10).place(x=300, y=92)

    def search_employee(self):
        i = 0
        for customer in self.customer_details:
            print(self.search_id.get())
            print(customer[0])
            if self.search_id.get() == customer[0]:
                 self.create_new_win(customer)
                 break
            else:
                i += 1
        else:
            messagebox.showerror("ERROR","No such customer on the database.")

    def create_new_win(self, customer):
        new = Tk()
        new.title("Customer Details")
        new.geometry('600x450')
        new.config(background="#e0e0e0")

        main_title = Label(new, text="Details About Customer", font=("Times New Roman", 16, "underline"),
                            bg="#4169E1",
                            fg="white", width="46",
                            height="2").place(x=18, y=20)

        details_line = ['Customer ID','Name', 'Email','Contact']
        y=100
        count=0
        for details in customer:
            Label(new, text=details_line[count], font=("Times New Roman", 16),bg="#e6e6e6", fg="#4169E1",
                            activebackground="#4169E1", activeforeground="white",
                            state=ACTIVE, width = 15).place(x=10, y=y)
            Label(new, text = ":", font=("Times New Roman", 16), bg="#e6e6e6", fg="#4169E1",
                            activebackground="#4169E1", activeforeground="#000000",
                            state=ACTIVE).place(x=170, y=y)
            Label(new, text=details, font=("Times New Roman", 16)).place(x=220,y=y)
            y += 40
            count += 1

        new.mainloop()

