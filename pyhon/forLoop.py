a=[]
i=1
while i<=10:
    a.append(i*i)
    i=i+1
b=int(input("enter a key to find"))
for j in a:
    print(j)
    if(b==j):
     print("key is found")
     break
    
else:
    print("for loop ended")