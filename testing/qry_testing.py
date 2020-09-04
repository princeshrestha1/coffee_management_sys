from classes.database import *

class qry():
    def __init__(self):
        self.my_db= MyDb()

    def login(self, un, pw):
            qry = """SELECT * FROM users WHERE username = %s AND password = %s"""
            # values = (self.__username, self.__password)
            values = (un, pw)
            user = self.my_db.show_data_product(qry, values)
            if len(user) > 0:
                return True
            else:
                return False
a=qry()