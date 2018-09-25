__author__ = 'DELL'
import  pymysql
connection = pymysql.connect(host= 'localhost',user='<username>',passwd= '<password>',db='emp')
cursor= connection.cursor()
query = ('SELECT * FROM `emp` ')
cursor.execute(query)
data = cursor.fetchall()
print(data)
query2= ('UPDATE `emp`  SET `sal` = `sal` +1000')
cursor.execute(query2)
data2 = cursor.fetchall()
print(data2)
