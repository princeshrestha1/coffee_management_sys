import pymysql
# Open database connection
db = pymysql.connect("localhost","testuser","test123","coffeemanagementsystem" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO products(id,
   name, type,company, cost)
   VALUES (2, 'capacuino', 'coffee', 'nescafe', 450)"""

   # Execute the SQL command
cursor.execute(sql)
   # Commit your changes in the database
db.commit()
print('mysql updated')

   # Rollback in case there is any error
db.rollback()
# disconnect from server
db.close()
