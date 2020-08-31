from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from coffee_product import Products


# from product_details import show_product


class ProductView:
    def __init__(self):
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
        self.update_btn.grid(row=5, column=0)

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
        selected_row = self.product_tree.selection()[0]
        self.selected_row = self.product_tree.products(selected_row, 'text')
        selected_data = self.product_tree.products(selected_row, 'values')
        index = product_tree.index(selected_row)
        all_product = product.show_products()
        selected_row= all_product[index]
        # selected_product = all_product[row[-1]]
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_data[0])

        self.entry_type.delete(0, END)
        self.entry_type.insert(0, selected_data[1])

        self.entry_cost.delete(0, END)
        self.entry_cost.insert(0, selected_data[2])

        self.entry_company.delete(0, END)
        self.entry_company.insert(0, selected_data[3])

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

    def delete_products(self):
        pass
        ''''garnu parne xa'''

    def show_products_tree(self):
        # product = Products()
        self.product_tree.delete(*self.product_tree.get_children())
        all_products = self.product.show_products()
        for i in all_products:
            #print(i)
            #print(type(i))
            self.product_tree.insert("", "end", text=i[0], values=(i[1], i[2], i[4],i[3]))

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

    # malai login page ma login succesful vaisakesi ok click garda coffee_home_page ma add products, add sales, product detail vaneko view products jun tala
    # ko bata start garxau treeview le from product_tree, tesaigari lastma product_sale_details banauni jasma customer id search garera total coffee sale details pauni
    # 1. yo .py ma submit button click garda def show_product_tree arko window ma khulne bananune junki Product details ma aawos, product add vako show hos

    # def move_to_product_details():
    # win.destroy()
    # n = Tk()
    # show_product(n)
    # n.mainloop()


ProductView()
