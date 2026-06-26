l=[1,2,3,4,5,6,7]
temp1=l[0]
temp2=l[1]
for i in range(len(l)-2):
    l[i]=l[i+2]
l[-1]=temp2
l[-2]=temp1
print(l)