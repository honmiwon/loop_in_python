num=int(input("enter the number"))
i=1
while i<=num:
    j=num
    while j>=i:
        print("#",end="")
        j-=1
    print()
    i+=1    