import math
c=5
h=30
l=[]
n=int(input("enter the number of numbers:"))
for i in range(n):
    d=int(input())
    l.append(d) 
#print(l)
for j in range(len(l)):
    s=(2*c*l[j])/h
    result=math.sqrt(s)
    print(result,end=" ")
