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


OrderView()'''
