from tkinter import *
import viewcustomer
import view_sales
from classes.add_sales import AddSales
from classes.add_product import ProductView

class Home:
    def __init__(self):
        self.win =Tk()
        self.win.geometry("600x565")
        self.win.title("Coffee Management System Dashboard")
        self.win.resizable(False, False)
        self.win.config(background="#e0e0e0")
        self.create_fields()

    def create_fields(self):
        main_title = Label(self.win, text="System Dashboard", bg="#d19063", font=("Times New Roman", 16, "underline"),
                           height="2", width="52").grid(row=0, column=2, pady=16)
        Button(self.win, text="Add Product", command= self.adproduct, font=("Times New Roman", 16),
               bg="#735039", fg="white", activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34", height="2").place(x=90, y=100)


        Button(self.win, text="Add Sales", command= self.adsales, font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90,
                                 y=180)

        Button(self.win, text="View Sales", command=self.viewsale, font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90, y=260)

        Button(self.win, text="Add Customer", command= self.cusdepage, font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90, y=340)
        Button(self.win, text="View Customers", command= self.view_customer, font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90, y=420)


    def adproduct(self):
        # import add_product
        ProductView()

    def cusdepage(self):
        import add_customer_details

    def view_customer(self):
        viewcustomer.View()

    def adsales(self):
        AddSales()

    def viewsale(self):
        view_sales.SaleDetails()














