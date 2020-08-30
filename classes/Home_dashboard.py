from tkinter import *
import viewcustomer


class Home:
    def __init__(self, window):
        self.win = window
        self.win.geometry("600x575")
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
               width="34", height="2").place(x=90, y=90)

        Button(self.win, text="Product Details", command=self.productdetails, font=("Times New Roman", 16), bg="#735039",
               fg="white", activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90, y=170)

        Button(self.win, text="Add Sales", command= self.adsales, font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90,
                                 y=250)  # add_sales bata sales garna sakne window banaunxau jasma customer name ra id details add garinxa,
        # then add garesi arko win khulxa ra tesma choose product option aaunxa , choose garesi automatically sab product details tree view ma show hunxa
        # ra save order button rakhnu parxa, save order click garesii yo products haru databse ma store hunuparxa

        Button(self.win, text="Sale Details", font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90, y=330)
        # sales details choose garesi sab customer ko sales record with their order tree view ma show hune ra each ko view order action button rakhne
        # jasle tyo customer ko order haru view hos another win ma with total cost
        Button(self.win, text="Add Customer", command= self.cusdepage, font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90, y=410)
        Button(self.win, text="View Customers", command= self.view_customer, font=("Times New Roman", 16), bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white", state=ACTIVE,
               width="34",
               height="2").place(x=90, y=490)


    def adproduct(self):
        # import add_product
        from add_product import ProductView
        ProductView()

    def cusdepage(self):
        import add_customer_details

    def view_customer(self):
        viewcustomer.View()

    def adsales(self):
        from add_sales import AddSales
        AddSales()



    def productdetails(self):
        pass


