n=int(input("Enter a number of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end="")
    for k in range(2*(i-1)):
        print("*",end="")
    for l in range(n-i+1,0,-1):
        print(l,end="")
    print()
