# yesma chai order add vako show huney banaune
from tkinter import *
from tkinter import ttk


class SaleDetails:
    def __init__(self):
        self.win = Tk()
        self.win.title('Order Products')
        self.win.geometry('486x430')
        self.win.config(background="#dabc98")
        self.create()
        self.win.mainloop()

    def create(self):
        self.product_tree = ttk.Treeview(self.win, columns=("customer_name", "customer_cell", "date", "action"))
        self.product_tree.place(height= 430, x=0, y=0)
        self.product_tree['show'] = 'headings'
        self.product_tree.heading("customer_name", text='Customer Name')
        self.product_tree.heading("customer_cell", text='Customer Contact')
        self.product_tree.heading("date", text='Date')
        self.product_tree.heading("action", text='Action')
        self.product_tree.column("customer_name", width=120)
        self.product_tree.column("customer_cell", width=120)
        self.product_tree.column("date", width=120)
        self.product_tree.column("action", width=120)

        self.product_tree.insert("", "end", text="a", values=['Leo', '98160XXXXX', '2020-08-31', 'View Order'])



SaleDetails()
