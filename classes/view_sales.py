# yesma chai order add vako show huney banaune
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql



class SaleDetails:
    def __init__(self):
        self.win = Tk()
        self.win.title('Order Products')
        self.win.geometry('480x200+500+300')
        self.win.resizable(False, False)
        self.win.config(background="#dabc98")
        self.my_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="coffeemanagementsystem"
        )
        sql = "select * from orders"
        self.my_cursor = self.my_connection.cursor()
        self.my_cursor.execute(sql)
        self.orders = []
        results = self.my_cursor.fetchall()
        for i in results:
            self.orders.append(i)

        #print(self.orders)
        self.orderSearchWindow()
        self.win.mainloop()

    def orderSearchWindow(self):
        self.search_id = StringVar(self.win)
        Label(self.win, text="Enter Order ID", font=("Times New Roman", 16), bg="#dabc98").place(x=30, y=49)
        Entry(self.win, text="Enter ID", textvariable=self.search_id, font=("Times New Roman", 16), width=24).place(x=28,
                                                                                                                   y=100)
        Button(self.win, text="Search", font=("Times New Roman", 16, "underline"), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", command=self.searchOrders, width=10).place(x=300, y=92)

    def searchOrders(self):
        print("in sale orders")
        #print(self.orders)
        i = 0
        for customer in self.orders:
            if str(self.search_id.get()) == str(customer[0]):
                self.create_win(customer)
                exit(0)
            else:
                i += 1
        else:
            messagebox.showerror("ERROR", "No such orders on the database.")

    def create_win(self, order):
        new = Tk()
        new.title("sale orders")
        new.geometry('600x325')
        new.config(background="#e0e0e0")
        main_title = Label(new, text="Details About order", font=("Times New Roman", 16, "underline"),
                           bg="#d19063",
                           fg="white",
                           activeforeground="white"
                           , width="46",
                           height="2").place(x=18, y=20)

        details_line = ['Customer ID', 'Name', 'Email', 'Contact', "Cost"]
        y = 100
        count = 0
        for details in order:
            Label(new, text=details_line[count], font=("Times New Roman", 16), bg="#735039", fg="white",
                  activebackground="#735039",
                  activeforeground="white",
                  state=ACTIVE, width=15).place(x=30, y=y)
            Label(new, text=":", font=("Times New Roman", 16), bg="#735039", fg="white",
                  activebackground="#735039",
                  activeforeground="white",
                  state=ACTIVE).place(x=190, y=y)
            Label(new, text=details, font=("Times New Roman", 16),bg="#e0e0e0").place(x=240, y=y)
            y += 40
            count += 1

        new.mainloop()
    # def create(self):
    #     self.product_tree = ttk.Treeview(self.win, columns=("customer_name", "customer_cell", "date", "action"))
    #     self.product_tree.place(height= 430, x=0, y=0)
    #     self.product_tree['show'] = 'headings'
    #     self.product_tree.heading("customer_name", text='Customer Name')
    #     self.product_tree.heading("customer_cell", text='Customer Contact')
    #     self.product_tree.heading("date", text='Date')
    #     self.product_tree.heading("action", text='Action')
    #     self.product_tree.column("customer_name", width=120)
    #     self.product_tree.column("customer_cell", width=120)
    #     self.product_tree.column("date", width=120)
    #     self.product_tree.column("action", width=120)
    #
    #     self.product_tree.insert("", "end", text="a", values=['Leo', '98160XXXXX', '2020-08-31', 'View Order'])



SaleDetails()