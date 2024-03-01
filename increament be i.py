n=int(input("enter a number:\n"))
num=0
r=0
for i in range(1,4,1):
    num=n%10
    r+=num+1
    n=n//10
print("sum:",r)
