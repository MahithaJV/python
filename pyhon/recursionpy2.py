def show(l,i=0):
    if(i==len(l)):
        return 0
    else:
        print(l[i])
        return show(l,i+1)

n=int(input("enter the no of numbers"))
l=[]
for a in range(n):
    m=int(input("enter element: "))
    l.append(m)
print("list :",l)

print(show(l))
