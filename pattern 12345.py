num=int(input("enter the number:"))
i=5
while i>=num:
    j=num
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i-=1  