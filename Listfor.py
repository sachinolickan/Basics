L1=[]
num=int(input("enter the number of elements"))
for i in range(num):
    x=int(input())
    L1.append(x)
print(L1)
p=int(input("enter the position from which the element to be removed"))
q=int(input("enter the new number"))
for j in range(0,len(L1)):
       if p==j:
        L1.remove(L1[p])
        L1.insert(p,q)
print(L1)

