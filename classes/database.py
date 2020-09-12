import pymysql

class MyDb:
    def __init__(self):
        self.my_connection = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="coffeemanagementsystem"
                        )
        self.my_cursor = self.my_connection.cursor()

    def iud(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def insert_with_id_return(self, qry, values):
        try:
            self.my_cursor.execute(qry, values)
            self.my_connection.commit()
            return self.my_cursor.lastrowid
        except Exception as e:
            print(e)
            return 0

    def show_data(self, qry):
        data = []
        try:
            self.my_cursor.execute(qry)
            data = self.my_cursor.fetchall()
            print(data)
            return data
        except Exception as e:
            print(e)
            return data

    def show_data_product(self, qry, values):
        data = []
        try:
            self.my_cursor.execute(qry, values)
            data = self.my_cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return data


