a=[1,2,3,4,5,6,7]
n=6
low=0
high=len(a)-1
while(low<=high):
    mid=(low+high)//2
    if a[mid]==n:
        print(mid)
        break
    elif n>a[mid]:
        low=mid+1
    else:
        high=mid-1



