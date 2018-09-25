__author__ = 'DELL'
f= lambda b,p : b**p
print(f(2,4))
num=100
t=True

f= filter(lambda i : not 100%i ,range(1,100))
print(list(f))

#to convert to dec to bin, hex and octal

n =int(input("Enter a number"))
print(bin(n))
print(hex(n))
print(oct(n))

#ASCII VALUE:
print(ord(str(n)))

#HCF & GCD:
x=9
y=6
def hcf(x,y):
    if x>y:
        x,y=y,x
    while y:
        x,y = y , x%y
    return x
print("GCD",hcf(x,y))

print("LCM ",hcf(x,y)*x)
#CALENDAR:
import calendar

mm=4
yy=2018
print("",calendar.month(yy,mm))