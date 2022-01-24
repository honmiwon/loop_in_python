n=int(input("enter the number"))
sum=0
temp=n
z=len(str(temp))
while temp>0:
    r=temp%10
    sum=sum+(r**z)
    temp=temp//10
if sum==n:
    print("it is an armstong number")
else:
    print("not an armstrong number")        