arr=[10,5,2,6]
k=100
l,r,m,s=0,0,0,0
c=0
while r<len(arr):
    s*=arr[r]
    while s>=k:
        s//=arr[l]
        l+=1
    length=r-l-1
    m=max(m,length)
    r+=1
    c+=1
print(c)