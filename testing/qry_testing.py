from classes.database import *

class qry():
    def __init__(self):
        self.my_db = MyDb()

    def login(self, un, pw):
        qry = """SELECT * FROM users WHERE username = %s AND password = %s"""
        # values = (self.__username, self.__password)
        values = (un, pw)
        user = self.my_db.show_data_product(qry, values)
        if len(user) > 0:
            return True
        else:
            return False

    def show_products(self):
        qry = "SELECT * FROM products"
        products_data = self.my_db.show_data(qry)
        return products_data

    def add_customer(self, customer_id, customer_name, email, contact):
        qry = "INSERT INTO customer_details (customer_id,customer_name, email, contact) VALUES (%s,%s,%s,%s)"
        values = (customer_id, customer_name, email, contact)
        if self.my_db.iud(qry, values):
            return True
        else:
            return False

    def delete_order(self, id):
        qry = '''delete from orders WHERE id=%s'''
        values = (id,)
        return self.my_db.iud(qry, values)


    def search_customer(self,name):
        qry = '''select * from customer_details where customer_name=%s'''
        values = (name,)
        b = self.my_db.iud(qry, values)


a = qry()
