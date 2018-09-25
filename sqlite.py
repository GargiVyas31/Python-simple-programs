__author__ = 'DELL'
import sqlite3
con = sqlite3.connect("emp.db")
c= con.cursor()
#query = "create table dept(dno INT ,dname VARCHAR(10))"
#query2 = "insert into dept VALUES(1,'COMPS')"
query4 = "insert into dept VALUES(2,'IT')"
#c.execute(query)
#c.execute(query2)
c.execute(query4)
query3= "select * from dept"
c.execute(query3)
r= c.fetchone()
while r is not None:
    print(r)
    r=c.fetchone()
    #con.commit()