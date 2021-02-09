from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import mysql.connector
import psycopg2

mydb = psycopg2.connect(
    host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

#mydb = mysql.connector.connect(
#    host="localhost",
#    user="root",
#    database="java"
#)

mycursor = mydb.cursor()


sql = "SELECT * FROM elabdata"
mycursor.execute(sql)
mobile_records = mycursor.fetchall()
for row in mobile_records:
    for j in row:
        print("->", j)
    print()

mydb.commit()



