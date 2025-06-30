"""reversing a list
i,a=1,[]
while i<=5:
    b=int(input("enter number"))
    a.append(b)
    i+=1
print(a)
# reversing a list
b=[]
j=len(a)-1
while j>=0:
    b.append(a[j])
    print(a[j])
    j-=1
print("end of loop")
print(a)
print(" i am b",b)"""

""" fibbonavvi num of n
n=int(input("enter the reqired nth fibonacci number:"))
f,s,i=1,2,1
while i<=n:
    next=f+s
    f=s
    s=next
    i+=1
print("the fibbonacci num is:",next)"""
food=input("enter type of food: ")
print("good" if food=="egg rice" else "bad bro!" )
class Student:
    def __init__(self, name, a):
        self.name = name
        self.list = a

    def avg(self):
        total = 0
        for b in self.list:
            total += b
        print("Average is:", total // len(self.list))  # use len for safety

s1 = Student("mahitha", [10, 10, 10])
print(s1.name)
s1.avg()
