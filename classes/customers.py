from classes.database import *


class Customer:
    def __init__(self):
        self.my_db = MyDb()

    def add_customer(self, customer_id, customer_name, email, contact):
        qry = "INSERT INTO customer_details (customer_id,customer_name, email, contact) VALUES (%s,%s,%s,%s)"
        values = (customer_id, customer_name, email, contact)
        if self.my_db.iud(qry, values):
            return True
        else:
            return False

