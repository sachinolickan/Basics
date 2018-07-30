L1=[[1,3],[4,2]]
L2=[[5,7],[8,6]]
R=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        R[i][j]+=L1[i][j]+L2[i][j]
print(R)
