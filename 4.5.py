__author__ = 'DELL'
punc= '''/?,<.>;:"'{[}]\|!~`&*()%$#@-_'''
my_str= "He said!!! with a lot of excitement that ------ I am MAD **"
string = ' '
for  char in my_str :
    if char not in punc :
        string = string + char

print(string)
