def avg(a=3,b=3,c=3):
    sum=a+b+c
    a=sum/3
    return a
print(avg(12,34,45))
print(avg())
print(avg(12,0))

#sum
def sum(a=0,b=0):
    return(a+b)
print(sum(2,3))#5
print(sum())#0
print(sum(1))#1

def sum(a,b=0):
    return(a+b)
print(sum(2,3))#5
print(sum(1))#1

def sum(a=0,b):
    return(a+b)
print(sum(2,3))#5
print(sum(1))# error


