# install Mysql on your computer
# https://dev.mysql.com/downloads/installer
# pip3 install mysql
# pip3 install mysql-connector
# pip3 install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(host="localhost", user="root")


# prepare a cursor object

cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE seou_db")

print("All Done!")
