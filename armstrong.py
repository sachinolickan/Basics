num=input("enter the number:")
sum=0
power=len(num)
for digit in num:
    sum+=int(digit)**power
if (sum==int(num)):
    print(int(num),"is an armstrong number")
else:
    print(int(num),"is not an armstrong number")
        
