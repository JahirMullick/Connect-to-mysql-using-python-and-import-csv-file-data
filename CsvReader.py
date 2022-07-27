'''
Connect to mysql using python 
and import the csv file into mysql 
and create a table.


System requirements :
Install the pydrive python module as follows :
pip install mysql-connector-python
pip install pandas

Install MySQL : 
MySQL Workbench with mysql
'''


# First Run Below Code then comment this and run next code
# Create A database in Mysql ------>

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='j@hirMj123')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE NEWDATASAMPLE")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
