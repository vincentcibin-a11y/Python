nums1=[4,1,2]
nums2=[1,3,4,2]
a=[]
for i in range(0,len(nums1)-1):
    for j in range(0,len(nums2)-1):
        if nums1[i]==nums2[j]:
            if(nums2[j]<nums2[j+1]):
                a.append(nums2[j+1])
            elif()
            else:
                a.append(-1)
print(a)
