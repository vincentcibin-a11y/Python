l=[9,8,4,7,6,4,0,5,8,1,11]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
max,ele=0,0
sl,ele1=0,0
for i in d:
    if d[i]>max:
        max=d[i]
        ele=i
for j in d:
    if d[j]>sl and j!=ele:
        sl=d[j]
        ele1=j
print(ele)
print(ele1)

