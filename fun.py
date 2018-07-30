total=10
def fun(n):
    global total
    total=total+n
    print("LOCALS====>",locals())
fun(5)
print(total)
print(globals())
