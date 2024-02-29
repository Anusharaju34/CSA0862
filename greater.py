n=int(input("enter number:"))
m=int(input("enter  sec num:"))
p=int(input("enter third num:"))
if(n>m):
    if(n>p):
        print(n,"greater number ")
    else:
        print(p,"greater number")
elif(m>p):
     print(m,"greater number")
else:
    print(p,"greater number")
