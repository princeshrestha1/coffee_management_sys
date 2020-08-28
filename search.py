from tkinter import *
import mysql.connector
from tkinter import ttk,messagebox

try:
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='assign',
    )
    cur = con.cursor()

except mysql.connector.Error as e:
    print(e)


class search:
    def __init__(self):
        self.root = Tk()
        self.root.title("Search for students")
        self.root.geometry('700x300')
        self.root.resizable(False,False)
        self.frame = Frame(self.root, bd=4, relief=RIDGE)
        self.frame.pack()

        self.table_frame = Frame(self.root, bd=4, bg='gray', relief=RIDGE)
        self.table_frame.pack()

        # self.sortby = Label(self.frame, text='Sortby',font='times 12 bold italic').grid(row=0, column=0, padx=10, pady=15)
        self.searchlbl = Label(self.frame, text='Search By',font='times 12 bold italic').grid(row=0, column=0, padx=10, pady=15)
        self.searchby = Label(self.frame, text='Search Text',font='times 12 bold italic').grid(row=1, column=0, padx=10, pady=15)

        self.entrysea = Entry(self.frame,bd=4,font='arial 10  italic')
        self.entrysea.grid(row=1, column=1, padx=15, pady=15)

        self.search = ttk.Combobox(self.frame, font=('arial 10 bold italic'), state='readonly',width=19)
        self.search['values'] = ('ID','Fname', 'lname')
        self.search.grid(row=0, column=1, pady=10, padx=20)

        self.button4 = Button(self.frame, text='Search', font='times 12 bold italic', command=self.searching, width=10,
                              height=1)
        self.button4.grid(row=2,column=0)

        self.button6 = Button(self.frame, text='Refresh', font='times 12 bold italic', command=self.refresh, width=10,
                              height=1)
        self.button6.grid(row=2,column=1)


        # ==============Table=================
        self.student_table = ttk.Treeview(self.table_frame,
                                          column=('id', 'fname', 'lname', 'age','gender', 'deg', 'address', 'number'))

        self.student_table.heading('id', text='ID')
        self.student_table.heading('fname', text='Fname')
        self.student_table.heading('lname', text='lname')
        self.student_table.heading('age', text='Age')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('deg', text='Degree')
        self.student_table.heading('address', text='Address')

        self.student_table.heading('number', text="Number")
        self.student_table['show'] = 'headings'
        self.student_table.pack()

        self.student_table.column('id', width=50)
        self.student_table.column('fname', width=80)
        self.student_table.column('lname', width=80)
        self.student_table.column('age', width=60)
        self.student_table.column('gender',width=80)
        self.student_table.column('deg', width=150)
        self.student_table.column('address', width=80)
        self.student_table.column('number', width=70)

        self.show()

        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.student_table.pack(fill=BOTH, expand=True)



    def show(self):
        query = 'select * from btable'
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def searching(self):
        find = self.entrysea.get()
        box = self.search.get()
        if not box:
            messagebox.showinfo('Info', 'No valid data found.Choose from option')
        elif not find:
            messagebox.showinfo('Info', 'No value inserted.')
        else:
            query1 = " select * from btable "
            cur.execute(query1)
            table = cur.fetchall()

            rows = self.linear_search(table, find)

            print(rows)
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())

            for row in rows:
                self.student_table.insert('', END, values=row)

            if not rows:
                messagebox.showinfo("Info", 'No data found in the database.')




    def linear_search(self, combo, find):
        try:

            if self.search.get() == 'Fname':
                column = 1

            elif self.search.get() == 'lname':
                column = 2

            elif self.search.get() == 'Address':
                column = 6

            elif self.search.get() == 'Age':
                column = 3
                find = int(find)

            elif self.search.get() == 'Gender':
                column = 4

            elif self.search.get() == 'Degree':
                column = 5

            elif self.search.get() == 'ID':
                find = int(find)
                column = 0


            else:
                column = 7

            found_list = []
            for row in combo:
                if row[column] == find:
                    found_list.append(row)

            return found_list

        except ValueError:
            messagebox.showinfo('Info', 'No valid data selected. ')

    def refresh(self):
        self.show()

    def pointer(self,event):
        try:
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']

        except IndexError:
            pass


if __name__ == '__main__':


    abc = search()
    mainloop()