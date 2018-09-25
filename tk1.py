__author__ = 'DELL'
from tkinter import *
root=Tk()
c=Canvas(root,width=1768,height=768,cursor='pencil')
id1=c.create_rectangle(600,350,800,650,fill='yellow',outline='black',activefill='green')
id2=c.create_line(600,350,700,150,fill='black')
id3=c.create_line(800,350,700,150,fill='black')
id4=c.create_rectangle(680,600,720,650,outline='black',width=3)
c.pack()
root.mainloop()
