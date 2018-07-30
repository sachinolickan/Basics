str=input("enter sentance:")
c=0
for char in range(len(str)):
    if(str[char]!=" "):
        c+=1
print("number of charcters:",c)
L=str.split(" ")
d=len(L)
print("number of words:",d)
   
