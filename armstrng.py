n=eval(input("enter number:"))
org=n
sum=0
while(n>0):
    a=n%10
    sum =sum+a*a*a
    n=n//10
    if(sum==org):
        print ("armstrong number")
    else:
        print("not armstrong number")
    
      
    
