n=int(input("enter the number:-7"))
i=2
j=0
while i<=n/2:
    if n%i==0:
        j=1
        # break
    i+=1
if j==0:
    print("it is prime") 
else:
    print("not prime") 
 