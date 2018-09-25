__author__ = 'DELL'
from tkinter import *
root=Tk()
root.title("Login Form")
class Form:
    ro=0
    def __init__(self,root):
        ro=root
        self.var1=IntVar()
        self.var2=IntVar()
        self.f=Frame(root,height=1000,width=1000)
        self.f.propagate(0)
        self.f.pack()
        self.l1=Label(self.f,text="Login:",height=4,width=20)
        self.l1.grid(row=0,column=0)
        self.l2=Label(self.f,text="Password:",height=4,width=20)
        self.l2.grid(row=0,column=4)
        self.b1=Button(self.f,text='OK',height=4,width=8,command=self.display)
        self.b1.grid(row=0,column=6)
        self.b1=Button(self.f,text='RESET',height=4,width=8,command=self.clear)
        self.b1.grid(row=0,column=8)
        self.e1=Entry(self.f,width=25)
        self.e1.grid(row=0,column=2)
        self.e2=Entry(self.f,width=25,show='*')
        self.e2.grid(row=0,column=5)



    def display(self):
        e1=self.e1.get()
        e2=self.e2.get()
        self.t=Text(Form.ro,width=100,height=100,font=('Verdana',-15,'bold'),wrap='word')
        self.t.insert(END,'\nYOUR NAME:'+e1)
        self.t.insert(END,'\nYOUR PASSWORD:'+e2)
        self.t.pack()
       # self.t.pack(SIDE="LEFT")
    def clear(self):
        e1=self.e1.delete(0,END)
        e2=self.e2.delete(0,END)



mb=Form(root)
root.mainloop()
