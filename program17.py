l=[1,2,3,4,5,6,7,8]
n=len(l)
i=0
j=(n//2)-1
for i in range(n//4):
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)
