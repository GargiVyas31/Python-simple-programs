'''__author__ = 'DELL'
#multiplication table
n=int(input("Enter the number"))
for i in range(1,11):
    print(i*n)

#Fibonacci
a=0
b=1
print("Fibonacci")
print(a)
print(b)
for i in range(3,10):
    c=a+b
    print(c)
    a,b=b,c

#Armstrong number

num = int(input("Enter a number"))
def armstrong(num):
    temp = num
    sum=0
    while temp >0 :
        r= temp%10
        sum = sum+ r**3
        temp=temp//10

    if num == sum :
        print("Armstrong number",num)
    ''''''else:
        print("Not an armstrong number")''''''
armstrong(num)

# Armstrong in a range
result= filter(lambda x : armstrong(x),range(1,200) )
print(list(result))

#sum of natural numbers:

import functools
#reduce returns an integer object
summ = ((functools.reduce(lambda x, y : x+y, range(1,101))))
print(summ)'''


#solving a quadratic:

a= int(input("Enter a"))
b= int(input("Enter b"))
c= int(input("Enter c"))

if b**2-4*a*c < 0:
    print("Imaginary roots")
else:
    d= b**2-4*a*c
    r1= -b//2*a - d**0.5//2*a
    r2= -b//2*a + d**0.5//2*a
    print(r1)
    print(r2)

import random
print(random.random()*100)















