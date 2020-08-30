'''yesma customer name ra customer number add garni euta frame ma ra arko ma choose product combo box
ma rakhera add garni, add gares teii tala items added to cart sucesffully message show gari product ra cost show garni ra lastma save order garni btn'''


'''from tkinter import *
from tkinter import ttk
from coffee_product import Products



class OrderView:
    def __init__(self):
        self.win = Tk()
        self.win.title('Order Products')
        self.win.geometry('500x320')
        self.product = Products

        self.label_id = Label(self.win, text='Customer id')
        self.label_id.grid(row=0, column=0)

        self.label_product = Label(self.win, text='Product')
        self.label_product.grid(row=1, column=0)

        self.combo_product = ttk.Combobox(self.win, state='readonly')
        self.combo_product.grid(row=1, column=1)

        self.label_type = Label(self.win, text='Type')
        self.label_type.grid(row=2, column=0)

        self.label_company = Label(self.win, text='Company')
        self.label_company.grid(row=3, column=0)

        self.label_cost = Label(self.win, text='Cost')
        self.label_cost.grid(row=4, column=0)

        self.show_products_in_combo()

        self.win.mainloop()

    def show_products_in_combo(self):
        data = self.product.show_products()
        self.combo_product['value'] = data


OrderView()
'''
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class AddSales:
    def __init__(self):
        self.win = Tk()
        self.win.title('Order Products')
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

        self.customer = Label(
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
            text="Choose Product", bg="#dabc98"
        )
        self.chooseProduct.place(x=10, y=100)
        self.products = ['capacuinno', 'espresso', 'latte', 'black']

        self.opt = Combobox(self.win, values=self.products, state = 'readonly')
        self.opt.place(x=100, y=100)

        self.productAdd = Button(
            text="Add",
            command=self.productAdd, bg="#735039", fg="white", width=4,
            activebackground="#735039", activeforeground="white"
        )
        self.productAdd.place(x=250, y=97)

        self.product_tree = ttk.Treeview(self.win, columns=("name", "type", "cost", "company"))
        # self.product_tree.grid(row=6, column=0, columnspan=2)
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

    def clickButton(self):
        pass

    def productAdd(self):
        print(self.opt.get())
        self.product_tree.insert("", "end", text="a", values=[self.opt.get(), 'coffee', '200', 'Nescafe'])


AddSales()
