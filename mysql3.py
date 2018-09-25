__author__ = 'DELL'
import pymysql
connection = pymysql.connect(host= 'localhost',user='<username>',passwd= '<password>',db='emp')
cursor= connection.cursor()
q1 = ('CREATE TABLE EMP( ENO INT(4), Ename VARCHAR(20),Basic REAL(7)),HRA REAL(10),DA REAL(7),PF REAL(7),DNO INT(4)' )
q2 = ('CREATE TABLE DEPT( DNO INT(4),DNAME  VARCHAR(10)' )

