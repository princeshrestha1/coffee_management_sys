from tkinter import *
from tkinter import messagebox

mywindowd = Tk()
mywindowd.geometry("560x600")
mywindowd.title("Add Customer Details Page")
mywindowd.resizable(False, False)
mywindowd.config(background="#F8F8FF")

frame1 = Frame(mywindowd)
frame1.config(height=650, width=560, background="#e0e0e0")
frame1.place(x=0, y=0)

main_title1 = Label(frame1, text="Customer Details Form", font=("Times New Roman", 16, "underline"), bg="#d19063",
                    fg="white", width="42",
                    height="2").place(x=25, y=30)


customer_id = StringVar()
customer_name = StringVar()
email = StringVar()
contact = StringVar()


# address = StringVar(mywindowd)


def send_data():
        customer_id_info = str(customer_id.get())
        customer_name_info = customer_name.get()
        email_info = email.get()
        contact_info = str(contact.get())
        with open("customer_details.txt", "a+") as file:
            file.write(customer_id_info + ',')
            file.write(customer_name_info + ',')
            file.write(email_info + ',')
            file.write(contact_info + ',')
            # file.write(address_info + '\n')
        messagebox.showinfo("Done", "Customer Added")




def settozero():
    customer_id_entry.delete(0, END)
    customer_name_entry.delete(0, END)
    # address_entry.delete(0, END)
    email_entry.delete(0, END)
    contact_entry.delete(0, END)


customer_id_label = Label(frame1, text="Customer ID:", bg="white", fg="white", activebackground="#e0e0e0",
                          activeforeground="#000000", state=ACTIVE)
customer_id_label.place(x=21, y=129)
customer_name_label = Label(frame1, text="Customer Name:", bg="#e0e0e0")
customer_name_label.place(x=21, y=209)
email_label = Label(frame1, text="Email:", bg="#e0e0e0")
email_label.place(x=21, y=289)
contact_label = Label(frame1, text="Contact Number:", bg="#e0e0e0")
contact_label.place(x=21, y=369)

customer_id_entry = Entry(frame1, textvariable=customer_id, width="35")
customer_name_entry = Entry(frame1, textvariable=customer_name, width="35")
email_entry = Entry(frame1, textvariable=email, width="35")
contact_entry = Entry(frame1, textvariable=contact, width="35")

customer_id_entry.place(x=23, y=155)
customer_name_entry.place(x=23, y=235)
email_entry.place(x=23, y=315)
contact_entry.place(x=23, y=395)

submit_btn = Button(mywindowd, text="Add Here", width="15", height="2", command=send_data, bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white",
                    state=ACTIVE)
submit_btn.place(x=25, y=500)

quitButton = Button(mywindowd, text='Quit', width="15", height="2", command=mywindowd.quit, bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white",
                    state=ACTIVE)
quitButton.place(x=220, y=500)

reset = Button(mywindowd, text='Reset', width="15", height="2", command=settozero, bg="#735039", fg="white",
               activebackground="#735039",
               activeforeground="white",
               state=ACTIVE)
reset.place(x=410, y=500)

mywindowd.mainloop()
