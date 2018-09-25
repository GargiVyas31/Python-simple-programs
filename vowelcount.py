__author__ = 'DELL'
dic= {'a':0,'e':0,'i':0,'o':0,'u':0}

string = input("Enter a sentence")
for i in string:
    if i in dic.keys():
        dic[i]+= 1
print(dic)


