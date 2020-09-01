from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database import MyDb
from coffee_product import Products



# from product_details import show_product


class ProductView:
    def __init__(self):
        self.my_db= MyDb()
        self.win = Tk()
        self.win.title("Add Coffee Product")
        self.win.resizable(False, False)
        self.win.geometry('492x342')
        self.win.config(background="#dabc98")
        self.product = Products()
        self.selected_row = ""
        # self.row = []

        self.label_name = Label(self.win, text="Product Name:", bg="#dabc98")
        self.label_name.grid(row=0, column=0)

        self.entry_name = Entry(self.win)
        self.entry_name.grid(row=0, column=1, ipadx="30")

        self.label_type = Label(self.win, text="Product Type:", bg="#dabc98")
        self.label_type.grid(row=1, column=0)

        self.entry_type = Entry(self.win)
        self.entry_type.grid(row=1, column=1, ipadx="30")

        self.label_cost = Label(self.win, text="Product Cost:", bg="#dabc98")
        self.label_cost.grid(row=2, column=0)

        self.entry_cost = Entry(self.win)
        self.entry_cost.grid(row=2, column=1, ipadx="30")

        self.label_company = Label(self.win, text="Product Company:", bg="#dabc98")
        self.label_company.grid(row=3, column=0)

        self.entry_company = Entry(self.win)
        self.entry_company.grid(row=3, column=1, ipadx="30")

        self.submit_btn = Button(self.win, text="Submit Products", command=self.add_product, bg="#735039", fg="white",
                                 activebackground="#735039", activeforeground="white")
        self.submit_btn.grid(row=5, column=1)

        self.update_btn = Button(self.win, text="Update Products", command=self.update_products, bg="#735039",
                                 fg="white",
                                 activebackground="#735039", activeforeground="white")
        self.update_btn.place(x=20, y=84)


        self.delete_btn = Button(self.win, text="Delete Products", command=self.delete_products, bg="#735039",
                                 fg="white",
                                 activebackground="#735039", activeforeground="white")
        self.delete_btn.place(x=150, y=84)


        self.product_tree = ttk.Treeview(self.win, columns=("name", "type", "cost", "company"))
        self.product_tree.grid(row=6, column=0, columnspan=2)
        self.product_tree['show'] = 'headings'
        self.product_tree.heading("name", text='Name')
        self.product_tree.heading("type", text='Type')
        self.product_tree.heading("cost", text='Cost')
        self.product_tree.heading("company", text='Company')
        self.product_tree.column("name", width=120)
        self.product_tree.column("type", width=120)
        self.product_tree.column("cost", width=120)
        self.product_tree.column("company", width=120)

        self.show_products_tree()

        self.win.mainloop()

    def on_select(self, event):
        selected_row = self.product_tree.selection()
        self.selected_row = self.product_tree.item(selected_row, 'text')
        selected_data = self.product_tree.item(selected_row, 'values')

        #all_product = self.product.show_products()
        #selected_product= all_product[selected_index]
        #self.selected_row = selected_product[0]

        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_data[0])

        self.entry_type.delete(0, END)
        self.entry_type.insert(0, selected_data[1])

        self.entry_cost.delete(0, END)
        self.entry_cost.insert(0, selected_data[3])

        self.entry_company.delete(0, END)
        self.entry_company.insert(0, selected_data[2])

    def add_product(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        cost = self.entry_cost.get()
        company = self.entry_company.get()

        if self.validate():
            if self.product.add_products(name, type, cost, company):
                messagebox.showinfo("product", "Products added successfully")
                self.show_products_tree()
                # move_to_product_details()
            # product add vaesakesi product show hune
            else:
                messagebox.showinfo("Error", "Products are not submitted")

    def update_products(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        cost = self.entry_cost.get()
        company = self.entry_company.get()
        if self.product.update_products(self.selected_row, name, type, cost, company):
            messagebox.showinfo("Item", "Item Updated")
            self.show_products_tree()
        else:
            messagebox.showerror("Error", "Item cannot be Updated")

    def click_product(self,event):
        try:
            self.id = self.product_tree.item(self.product_tree.selection(),"values")[0]
        except Exception:
            pass


    def delete_products(self):
        try:
           if self.product.delete_products(self.selected_row):
               messagebox.showinfo("Delete ","Product Deleted ")
           self.show_products_tree()
        except Exception:
            pass

    def show(self):
        self.product_tree.delete(*self.product_tree.get_children())
        data= self.my_db.show_products











    def show_products_tree(self):
        # product = Products()
        self.product_tree.delete(*self.product_tree.get_children())
        self.all_products = self.product.show_products()
        for i in self.all_products:
            #print(i)
            #print(type(i))
            self.product_tree.insert("", "end", text=i[0], values=(i[1], i[2], i[3],i[4]))
        self.product_tree.bind("<Double-1>", self.on_select)

    def validate(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        cost = self.entry_cost.get()
        company = self.entry_company.get()

        if name == '' or type == '' or cost == '' or company == '':
            messagebox.showerror('Error', 'Please fill all the fields')
            return False
        elif not cost.isdigit():
            messagebox.showerror('Error', 'Invalid entry for cost')
            return False
        else:
            return True




