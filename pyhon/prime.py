n=int(input("enter a number up to which prime number needed: "))
p=[]
for b in range(2,n+1,1):
    for a in range(2,b,1):
        if(b%a==0):
            break
    else:
            p.append(b)

print("prime numbers are :",p)

            

