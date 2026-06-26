nums=[-1,0,3,5,9,12]
targets=8
l=0
h=len(nums)-1
while l<=h:
    mid=(l+h)//2
    if targets<nums[mid]:
        h=mid-1
    elif targets>nums[mid]:
        l=mid+1
    else:
        return mid
return -1
        

