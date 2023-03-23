from mysql.connector import Error
import mysql.connector as MC

try:
    connect = MC.connect(
        host = "localhost",
        user = "root",
        passwd = "Softex2023",
        database = "company"
    )

    print ("MySQL Database connection successful")

except Error as err:
    print ("Error: {}".format(err))

cursor = connect.cursor()

while True:
    a = input("O que você quer fazer:")

