a=[2,3,4,3,3,5,4]
count=0
for i in range(0,7):
    if a[i+1]>a[i]:
        count=count+1
print(count)
