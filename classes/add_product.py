from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database import MyDb
from coffee_product import Products



class ProductView:
    def __init__(self):
        self.my_db = MyDb()
        self.win = Tk()
        self.win.title("Add Coffee Product")
        # self.win.resizable(False, False)
        self.win.geometry('609x442')
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

        self.label_company = Label(self.win, text="Search Product:", bg="#dabc98")
        self.label_company.grid(row=12, column=0)

        self.entry_product = Entry(self.win)
        self.entry_product.grid(row=12, column=1, ipadx=10)

        self.product_btn = Button(self.win, text="Search Products", bg="#735039", fg="white",
                                  activebackground="#735039", activeforeground="white", command=self.search_product)
        self.product_btn.grid(row=15, column=1)

        self.show_all_btn = Button(self.win, text="Show All Products", bg="#735039", fg="white",
                                   activebackground="#735039", activeforeground="white", command=self.show_all_products)
        self.show_all_btn.grid(row=18, column=1)

        self.submit_btn = Button(self.win, text="Submit Products", command=self.add_products, bg="#735039", fg="white",
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

        self.product_tree = ttk.Treeview(self.win, columns=("id","name", "type", "company", "cost"))
        self.product_tree.grid(row=6, column=0, columnspan=2)
        self.product_tree['show'] = 'headings'
        self.product_tree.heading('id',text='id')
        self.product_tree.heading("name", text='Name')
        self.product_tree.heading("type", text='Type')
        self.product_tree.heading("cost", text='Cost')
        self.product_tree.heading("company", text='Company')
        self.product_tree.column('id', width=120)
        self.product_tree.column("name", width=120)
        self.product_tree.column("type", width=120)
        self.product_tree.column("cost", width=120)
        self.product_tree.column("company", width=120)
        self.product_tree.bind("<Double-1>", self.on_select)


        self.show_all_products()

        self.win.mainloop()

    def on_select(self, event):
        selected_row = self.product_tree.selection()
        self.selected_row = self.product_tree.item(selected_row, 'text')
        selected_data = self.product_tree.item(selected_row, 'values')




        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_data[1])

        self.entry_type.delete(0, END)
        self.entry_type.insert(0, selected_data[2])

        self.entry_cost.delete(0, END)
        self.entry_cost.insert(0, selected_data[4])

        self.entry_company.delete(0, END)
        self.entry_company.insert(0, selected_data[3])


    def add_products(self):

        qry = "INSERT INTO products (name,type,cost, company) VALUES (%s,%s,%s,%s)"
        values = (self.entry_name.get(),self.entry_type.get(),self.entry_cost.get(),self.entry_company.get())
        self.my_db.iud(qry, values)
        self.show_all_products()
        messagebox.showinfo("product", "Products added successfully")


    def update_products(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        cost = self.entry_cost.get()
        company = self.entry_company.get()
        if self.product.update_products(self.selected_row, name, type, cost, company):
            messagebox.showinfo("Item", "Item Updated")
            self.show_all_products()
        else:
            messagebox.showerror("Error", "Item cannot be Updated")

    def click_product(self, event):
        try:
            self.id = self.product_tree.item(self.product_tree.selection(), "values")[0]
        except Exception:
            pass

    def delete_products(self):
        qry = '''delete from products WHERE name=%s'''
        values = (self.entry_name.get(),)
        self.my_db.iud(qry, values)
        self.show_all_products()
        messagebox.showinfo("delete","Product deleted")



    def show(self):
        self.product_tree.delete(*self.product_tree.get_children())
        data = self.my_db.show_products

    def search_product(self):  # searching
        qry = '''(select * from products where id=%s)'''
        values = (self.entry_product.get(),)
        a = self.my_db.show_data_product(qry, values)
        if len(a) != 0:
            self.product_tree.delete(*self.product_tree.get_children())
            for row in a:
                self.product_tree.insert('', END, values=row)
        else:
            messagebox.showerror('Error', 'Enter Correct ID', parent=self.win)

    def show_all_products(self):
        qry = '''(select * from products)'''
        rows = self.my_db.show_data(qry)
        if len(rows) != 0:
            self.product_tree.delete(*self.product_tree.get_children())
            for row in rows:
                self.product_tree.insert('', END, values=row)



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
