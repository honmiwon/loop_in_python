n=int(input("enter the number"))
i=5
while i>=1:
    print(" "*(n-i),end=" ")
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i-1     