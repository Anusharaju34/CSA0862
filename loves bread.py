n=int(input("enter no of fresh loves purshace:"))
m=int(input("enter no off day old loves purshace:"))
reg=185.00
new=reg*n
old=111*m
print("regular price:",reg)
roun=format(new,".2f")
row=format(old,".2f")
print("amount new loves:",roun)
print("amount old leaves:",row)
total=new+old
tot=format(total,".2f")
print("total amount",total)
