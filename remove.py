L1=[]
num=int(input("enter the number of elements"))
for i in range(num):
    x=int(input())
    L1.append(x)
print(L1)
p=int(input("enter the number to delete"))
for j in L1:
    if(j==p):
        L1.remove(p)
print(L1)
