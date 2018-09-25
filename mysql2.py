__author__ = 'DELL'
import pymysql
connection = pymysql.connect(host= 'localhost',user='<username>',passwd= '<password>',db='emp')
cursor= connection.cursor()
emp_id = int(input("Enter the user id"))
query = ("SELECT * FROM `emp` WHERE `emp_id` = emp_id ")
result = cursor.execute(query)
print(result)

