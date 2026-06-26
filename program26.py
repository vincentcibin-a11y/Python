l=[9,8,4,7,6,4,0,5,8,1]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


