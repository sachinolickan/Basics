L=[("abi",1,"M",171),("anju",2,"F",160),("anu",3,"F",162),("arun",4,"M",170)]
L1=[]
L2=[]

for i in range(0,len(L)):
    if L[i][2]=="M":
        L1.append(L[i][3])
    elif L[i][2]=="F":
        L2.append(L[i][3])
avg1= sum(L1)/len(L1)
avg2= sum(L2)/len(L2)        
print("aveage of boys:",avg1)
print("average of girls:",avg2)


        
