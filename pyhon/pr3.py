# checking list contain aplindrome of numbetrs
list=[1,2,3,1]
tem=list.copy()
print(tem)
list.reverse()
if(list==tem):
    print("palindrome")
else:
    print("not a palindrome")