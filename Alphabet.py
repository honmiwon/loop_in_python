n=int(input("enter the number"))
i=0
while i<n:
    k=ord("A")+i
    j=0
    while j<=i:
        print(chr(k),end="")
        k=k+1
        j+=1
    i+=1
    print()    