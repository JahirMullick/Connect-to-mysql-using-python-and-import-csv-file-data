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




# Once the upper code is run sucessfully then run below code
# Send the data into the MySQL Database --------->

import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
empdata = pd.read_csv('sample.csv', index_col=False, delimiter = ',')
empdata.head()
try:
    conn = msql.connect(host='localhost', database='NEWDATASAMPLE', user='root', password='j@hirMj123')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS newdatasample_data;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE newdatasample_data(Organization varchar(255),CEO varchar(255),date varchar(255))")
        print("Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO NEWDATASAMPLE.newdatasample_data VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)
