L1=[[1,4,5],[6,2,7],[9,8,3]]
L2=[[2,4,6],[3,6,9],[4,3,2]]
R=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(L1[0])):
    for j in range(len(L2)):
        for k in range(len (L2[0])):
             R[i][j]+=L1[i][k]*L2[k][j]
            
       
print(R)
       
