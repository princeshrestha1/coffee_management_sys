from classes.database import *

from classes.database import MyDb

class User:

    def login(self, un, pw):
        self.db = MyDb()
        qry = """SELECT * FROM users WHERE username = %s AND password = %s"""
        # values = (self.__username, self.__password)
        values = (un, pw)
        user = self.db.show_data_product(qry, values)
        if len(user) > 0:
            return True
        else:
            return False
