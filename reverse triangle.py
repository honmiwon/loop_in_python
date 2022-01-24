i=5
while i>=1:
    print(""*(5-i),end="")
    j=1
    while j<=i:
        print("*",end="")
        j=1
        while j<=i:
            print("*",end="")
            j=j+1
        print()
        i=i-1    