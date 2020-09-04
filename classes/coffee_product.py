from classes.database import MyDb


class Products:
    def __init__(self):
        self.my_db = MyDb()


    # def add_products(self,name, type, cost, company):
    #     qry = "INSERT INTO products (name,type,cost, company) VALUES (%s,%s,%s,%s)"
    #     values = (name, type, cost, company)
    #     if self.my_db.iud(qry, values):
    #         return True
    #     else:
    #         return False

    def show_products(self):
        qry = "SELECT * FROM products"
        products_data = self.my_db.show_data(qry)
        return products_data

    def update_products(self, row, name, type, cost, company):
        qry = "UPDATE products SET name = %s, type = %s, cost = %s, company = %s WHERE id = %s"
        values = (name, type, cost, company, row)
        self.my_db.iud(qry, values)
        return True

    def delete_products(self,row):
        qry = "DELETE FROM products WHERE id=%s"
        values = (row,)
        self.my_db.iud(qry, values)
        return True

