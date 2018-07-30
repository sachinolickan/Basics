import copy
L1=[2,3,[5,6],7]
L2=copy.deepcopy(L1)
print("original elements before deepcopying in L1")
for i in range(0,len(L1)):
    print(L1[i],end=" ")
print("\r")
L2[2][0]=4
print("\r")
print("new elements in L2 ")
for j in range(0,len(L2)):
    print(L2[j],end=" ")
print("\r")
print("after deep copying in L1")
for i in range(0,len(L1)):
     print(L1[i],end=" ")
    
