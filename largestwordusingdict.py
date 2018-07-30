l=[]
d={}
s=""
max_len=0
x=input("enter the sentance:")
l=x.split()
for i in range(len(l)):
    d[i]=l[i]
l1=d.values()
for word in l1:
    if len(word)>max_len:
        max_len=len(word)
        s=word
print("longest word:",s)

   
