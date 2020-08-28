
from tkinter import ttk
from tkinter import *
from coffee_product import Products



class show_product:
    def __init__(self, master):
        self.master = master
        self.show_product_tree()

    def show_product_tree(self):
        self.master.title("Show Coffee Product Details")
        self.master.geometry('492x342')
        product_tree = ttk.Treeview(columns=("name", "type", "cost", "company"))
        product_tree.grid(row=6, column=0, columnspan=2)
        product_tree['show'] = 'headings'
        product_tree.heading("name", text='Name')
        product_tree.heading("type", text='Type')
        product_tree.heading("cost", text='Cost')
        product_tree.heading("company", text='Company')
        product_tree.column("name", width=120)
        product_tree.column("type", width=120)
        product_tree.column("cost", width=120)
        product_tree.column("company", width=120)
        product= Products()
        all_product = product.show_products()
        for i in all_product:
            product_tree.insert("", "end", text="a", values=i)



