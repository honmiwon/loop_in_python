n=5
k=0
for i in range(1,n):
    k+=i
    for j in range(k,k-i,-1):
        print(str(j)+"",end=" ")
    print()    