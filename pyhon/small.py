i,a=1,[]
while i<=5:
    b=int(input("enter number"))
    a.append(b)
    i+=1
print(a)
min=a[0]
for b in a:
    if(min>b):
        min=b
print("min num is",min)

max=a[0]
for b in a:
    if(max<b):
        max=b
print("max num is",max)
