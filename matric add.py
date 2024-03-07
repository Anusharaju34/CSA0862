a=[[1,5,1],[3,4,1]]
b=[[8,9,2],[7,2,2]]
c=[[0,0],[0,0]]
for i in range (len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j]=c[i][j][m]+a[i][k]*b[k][j]
for i in c:
    print (i)
        
