num=int(input("enter the  number:"))
i=1
sum=0
while(i<num):
    if(num%i==0):
        sum=sum+i
    i=i+1
print(num)
if(sum==num):
    print(num,"perfect Number")
else:
    print(num,"not a perfect Number")   
            