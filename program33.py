l=[2,1,3,2,4,5,6,6,6,1,4,7]
n=int(input("Enter the times"))
m=0
for i in range(0,len(l)):
    b=sum(l[i:i+n])
    m=max(m,b)
print(m)
    

