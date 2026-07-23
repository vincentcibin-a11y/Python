arr=[29,10,14,37,13]
n=len(arr)
for i in range(n):
    minimum=i
    for j in range(i+1,n):
        if(arr[j]<arr[minimum]):
            minimum=j
    arr[i],arr[minimum]=arr[minimum],arr[i]
print(arr)