l=[]
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
