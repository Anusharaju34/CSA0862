n=int(input("enter number"))
even=0
odd=0
for i in range (1,n+1):
    if(n%2==0):
        even+=i
    else:
        odd+=i
print("even:",even)
print("odd:",odd)
