s=input("enter the word:")
p=len(s)
st=""
for i in range(p,0,-1):
     st+=s[i-1]
if st==s:
    print("yes")
else:
    print("no")


