l=[]
c=1
num=int(input("enter no of elements:"))
for i in range(num):
    x=int(input())
    l.append(x)
num2=int(input("enter the number to search:"))
for j in range(len(l)):
    if(l[j]==num2):
        c=-1
        print("found")
        break
if(c==1):
    print("not found")
         

          
