from classes.database import *

class User:

    def __init__(self, un, pw, t, n):

        self.db = MyDb()

    def register(self, un, pw, t, n):
        qry = """INSERT INTO users (username, password, type, name)
                VALUES (%s,%s,%s,%s)"""

        values = (un, pw, t, n)
        return self.db.iud()
    def login(self, un, pw):
        qry = """SELECT * FROM users WHERE username = %s AND password = %s"""
        # values = (self.__username, self.__password)
        values = (un, pw)
        user = self.db.show_data_p(qry, values)
        if len(user) > 0:
            return True
        else:
            return False