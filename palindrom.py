n=int(input("Enter the number:"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if (temp==rev):
    print("It is a palindrom number!")
else:
    print("It is not a palindrom number!")        
