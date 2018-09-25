__author__ = 'DELL'
import os,shutil
#DELETE A FILE
filename = input("Enter the filename")
if os.path.isfile(filename):
    os.remove(filename)
else:
    print("File doesnot exist")

 #COPY FILE
source= input("Enter source file")
dest = input("Enter destination file")

shutil.copy(source,dest)

#MOVE FILE

source= input("Enter source file")
dest = input("Enter destination file")

shutil.move(source,dest)

