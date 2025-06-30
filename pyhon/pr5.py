"""# sum of frist n natural num
n=int(input("enter number: "))
i,sum=1,0
while i<n+1:
    sum=sum+i
    i=i+1
print("sum of frist",n,"is",sum)



#factorial of n using for loop
m=int(input("enter number:"))
pdt=1
for a in range(n,0,-1):
    pdt=pdt*a
print("factorial is done:",pdt)"""



# Checking if Armstrong number
n = int(input("Enter number: "))
sum = 0
i = n

while i > 0:
    r = i % 10
    sum = sum + (r ** 3)
    i = i // 10

print(sum == n)
