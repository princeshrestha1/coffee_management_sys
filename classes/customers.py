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

    '''def show_items(self):
        qry = "SELECT * FROM customer details"
        items_data = self.my_db.show_data(qry)
        return items_data
        # if len(items_data) > 0:
        #     return True
        # else:
        #     return False'''
