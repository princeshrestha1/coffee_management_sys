'''yesma customer name ra customer number add garni euta frame ma ra arko ma choose product combo box
ma rakhera add garni, add gares teii tala items added to cart sucesffully message show gari product ra cost show garni ra lastma save order garni btn'''


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox


class AddSales:
    def __init__(self):
        self.win = Tk()
        self.win.title('Order Products')
        self.win.resizable(False, False)
        self.win.geometry('486x430')
        self.win.config(background="#dabc98")
        self.draw_components()
        self.win.mainloop()

    def draw_components(self):
        self.__name = ""
        self.name = Entry(
            self.win,
            textvariable=self.__name,width=22
        )
        self.name.place(x=105, y=30)

        self.customer = Label(self.win,
            text="Customer Name", bg="#dabc98"
        )
        self.customer.place(x=10, y=30)

        self.addButton = Button(
            self.win,
            text="Add",
            command=self.clickButton, bg="#735039", fg="white", width= 4,
            activebackground="#735039", activeforeground="white"
        )
        self.addButton.place(x=250, y=27)

        self.chooseProduct = Label(
            self.win,
            text="Choose Product", bg="#dabc98"
        )
        self.chooseProduct.place(x=10, y=100)
        self.products_names = ['capacuino', 'espresso', 'Black', 'black', 'latte', 'mocha']
        self.products = {
            'capacuino': ["capacuino", "coffee", '480', 'lavazza'],
            'espresso': ["espresso", "coffee", '450', 'nescafe'],
            'Black': ["black", "coffee", '470', 'maxwell'],
            'black': ["black", "coffee", '380', 'maxwell'],
            'latte': ["latte", "coffee", '420', 'caribou'],
            'mocha': ["mocha", "coffee", '510', 'tim horton']
        }

        self.opt = Combobox(self.win, values=self.products_names, state = 'readonly')
        self.opt.place(x=100, y=100)

        self.productAdd = Button(
            self.win,
            text="Add",
            command=self.productAdd, bg="#735039", fg="white", width=4,
            activebackground="#735039", activeforeground="white"
        )
        self.productAdd.place(x=250, y=97)
        self.saveButton = Button(
            self.win,
            text="Save Order",
            command=self.saveThisOrder, bg="#735039", fg="white", width=8,
            activebackground="#735039", activeforeground="white"
        )
        self.saveButton.place(x=250, y=140)

        self.product_tree = ttk.Treeview(self.win, columns=("name", "type", "cost", "company"))
        self.product_tree.place(x=0, y=200)
        self.product_tree['show'] = 'headings'
        self.product_tree.heading("name", text='Name')
        self.product_tree.heading("type", text='Type')
        self.product_tree.heading("cost", text='Cost')
        self.product_tree.heading("company", text='Company')
        self.product_tree.column("name", width=120)
        self.product_tree.column("type", width=120)
        self.product_tree.column("cost", width=120)
        self.product_tree.column("company", width=120)



    def saveThisOrder(self):
        print("yeha db link garnu xa")

    def clickButton(self):
        pass

    def productAdd(self):
        if self.opt.get() != "":
            print(self.opt.get())
            self.product_tree.insert("", "end", text="a", values=self.products[self.opt.get()])
            messagebox.showinfo("Product", "Product Added for order")

        else:
            messagebox.showerror("Error", "Product not added")


