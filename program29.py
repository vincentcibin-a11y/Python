num=[1,3,2,2,5,2,3,7]
c=[]
for i in num:
    for j in num:
        if i-j==1:
            c.append(i)
            c.append(j)