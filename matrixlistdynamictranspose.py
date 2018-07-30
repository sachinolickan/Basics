l=[]
l1=[]
m=int(input("enter number of rows"))
n=int(input("enter number of columns"))
for i in range(m):
    l.append([])
for i in range(m):
    for j in range(n):
        l[i].append(j)
        l[i][j]=0
for i in range(m):
    for j in range(n):
        l[i][j]=int(input())
print(l)
for i in range(n):
    l1.append([])
for i in range(n):
    for j in range(m):
        l1[i].append(j)
        l1[i][j]=0
for i in range(n):
    for j in range(m):
        l1[i][j]=l[j][i]
print(l1)

        
        
