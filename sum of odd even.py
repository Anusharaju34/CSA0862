sumofodd=0
sumofeven=0
n=int(input("enter number:"))
for i in range (1,n+1,1):
    if(i%2==0):
       sumofeven+=i
    else:
        sumofodd+=i
print(sumofeven,"is the sum of even numb:")
print(sumofodd,"is the sum of odd numb:")
    

