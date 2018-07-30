from math import *
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
y=((b*b)-4*a*c)
if y<0:
    print("no real roots")
else:
    z=sqrt((b*b)-4*a*c)
    root1=(-b+z)/2*a
    root2=(-b-z)/2*a

    print("root1:",root1)
    print("root2:",root2)
