__author__ = 'DELL'
import sqlite3
from tkinter import *
root = Tk()

conn= sqlite3.connect('Student.db')

c= conn.cursor()

#q0 = 'create table student(name VARCHAR(10), id INT )'
#c.execute(q0)
'''
class Form:
    root=0
    def __init__(self,root):
        root= root
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.f= Frame(root,width=100,height=20)
        self.f.propagate()
        self.f.pack()

        self.l1= Label(self.f,text="Name",width=25,height=5)
        self.l1.grid(row=0,column=0)
        self.e1=Entry(self.f,width=25)
        self.e1.grid(row=0,column=2)

        self.l2=Label(self.f,text="Id",width=25,height=5)
        self.l2.grid(row=0,column=4)
        self.e2=Entry(self.f,width=25)
        self.e2.grid(row=0,column=6)

        self.b1=Button(self.f,text="Ok",width=20,height=3,command=self.insert)
        self.b1.grid(row=0,column=8)

        self.b2=Button(self.f,text="Display",width=20,height=3,command=self.display)
        self.b2.grid(row=0,column=10)

        self.b3=Button(self.f,text="Reset",width=20,height=3,command=self.clear)
        self.b3.grid(row=0,column=12)

    def insert(self):
        e1= str(self.e1.get())
        e2= int(self.e2.get())

        q1= 'insert into student(name,id) VALUES(?,?)'
        #q2= 'insert into student(id) VALUES(?)'
        c.execute(q1,(e1,e2,))
        #c.execute(q2,(e2,))
        conn.commit()



    def display(self):

        e1=self.e1.get()
        e2=self.e2.get()
        self.t=Text(Form.root,width=100,height=100,font=('Verdana',-15,'bold'),wrap='word')
        self.t.insert(END,'\nYOUR NAME:'+e1)
        self.t.insert(END,'\nYOUR ID:'+e2)
        self.t.pack()

    def clear(self):
        e1=self.e1.delete(0,END)
        e2=self.e2.delete(0,END)


query3= "select * from student"
c.execute(query3)
r= c.fetchone()
while r is not None:
    print(r)
    r=c.fetchone()'''
num =5

c.execute("update student set id=5 where id=(?) ",(num,))
c.execute("select * from student where id=(?) ",(num,))
r= c.fetchone()
print(r)

#form = Form(root)
root.mainloop()







