from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from coffee_product import Products
#from product_details import show_product


class ProductView:
    def __init__(self):
        self.win = Tk()
        self.win.title("Add Coffee Product")
        self.win.geometry('492x342')
        self.product = Products()
        self.row = []

        self.label_name = Label(self.win, text="Product Name:")
        self.label_name.grid(row=0, column=0)

        self.entry_name = Entry(self.win)
        self.entry_name.grid(row=0, column=1, ipadx="30")

        self.label_type = Label(self.win, text="Product Type:")
        self.label_type.grid(row=1, column=0)

        self.entry_type = Entry(self.win)
        self.entry_type.grid(row=1, column=1, ipadx="30")

        self.label_cost = Label(self.win, text="Product Cost:")
        self.label_cost.grid(row=2, column=0)

        self.entry_cost = Entry(self.win)
        self.entry_cost.grid(row=2, column=1, ipadx="30")

        self.label_company = Label(self.win, text="Product Company:")
        self.label_company.grid(row=3, column=0)

        self.entry_company = Entry(self.win)
        self.entry_company.grid(row=3, column=1, ipadx="30")

        self.submit_btn = Button(self.win, text="Submit Products", command=self.add_product)
        self.submit_btn.grid(row=5, column=1)

        self.update_btn = Button(self.win, text="Update Products")
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

        self.win.mainloop()


    def on_select(self, event):
        #selected_product=product_tree.selection()[0]
        #row.append(product_tree.index(selected_row))
        selected_row = self.product_tree.selection()[0]
        selected_index = self.product_tree.index(selected_row)
        all_product= self.product.show_products()
        selected_product = all_product[selected_index]
        #selected_product = all_product[row[-1]]
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_product[0])

        self.entry_type.delete(0, END)
        self.entry_type.insert(0, selected_product[1])

        self.entry_cost.delete(0, END)
        self.entry_cost.insert(0, selected_product[2])

        self.entry_company.delete(0, END)
        self.entry_company.insert(0, selected_product[3])


    def add_product(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        cost = self.entry_cost.get()
        company = self.entry_company.get()
        if self.product.add_products(name, type, cost, company):
            messagebox.showinfo("product", "Products added successfully")
            self.show_products_tree()
            #move_to_product_details()
        # product add vaesakesi product show hune
        else:
            messagebox.showinfo("Error", "Products are not submitted")


    '''def update_product(self):
        if row[-1] < 0:
            messsagebox.showerror("Error", "No Row Selected")
        else:
            name= entry_name.get()
            type= entry_type.get()
            cost= entry_cost.get()
            company= entry_company.get()
            print(row)'''



    def show_products_tree(self):
        #product = Products()
        self.product_tree.delete(*self.product_tree.get_children())
        all_product = self.product.show_products()
        for i in all_product:
            self.product_tree.insert("", "end", text="a", values=i)

        self.product_tree.bind("<Double-1>", self.on_select)




    # malai login page ma login succesful vaisakesi ok click garda coffee_home_page ma add products, add sales, product detail vaneko view products jun tala
    # ko bata start garxau treeview le from product_tree, tesaigari lastma product_sale_details banauni jasma customer id search garera total coffee sale details pauni
    # 1. yo .py ma submit button click garda def show_product_tree arko window ma khulne bananune junki Product details ma aawos, product add vako show hos

    #def move_to_product_details():
        #win.destroy()
        #n = Tk()
        #show_product(n)
        #n.mainloop()





