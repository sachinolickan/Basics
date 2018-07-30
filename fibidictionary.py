d={1:1,2:1}
n=int(input("enter the nth number"))
for i in range(3,n+1,1):
    d[i]=d[i-1]+d[i-2]
print(d)   
print("nth fibonacci no:",d[n])
