nums=[2,7,11,15]
target=9
c=[]
for i in range(0,len(nums)):
    for j in range(0,i):
        if nums[i]+nums[j]==target:
            c.append(i)
            c.append(j)
print(c)
