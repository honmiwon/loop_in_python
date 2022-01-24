num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
rem=1
if num1 > num2:
    while rem!=0:
     rem=num1%num2
     if rem==0:
         hcf=num2
    else:
        num1=num2
        num2=rem
else:
    while rem!=0:
     rem=num2%num1
     if rem==0:
         hcf=num1
     else:
        num2=num1
        num1=rem
    print("HCF of two number is:",hcf)
    