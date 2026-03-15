import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nigam@db90",
    database = "school"
)

mycursor = mydb.cursor()

