import mysql.connector

 # connect to the mysql server
 # Replace he username and the password with your details
 connection = mysql.connector.connect(
   host="localhost",
   user="root",
   password="root"
 )

 # create a new database n the server
 cursor = Connect.cursor()
cursor.execute("CREATE DATABASE database_name")

 # or look at the list of database on the server 
 cursor.execute("SHOW DATABASES")
for db in cursor:
  print(db)

cursor.close
connection.close()
