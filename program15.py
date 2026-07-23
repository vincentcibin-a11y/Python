a=[7,7,1,8,1]
b=[]
count=0
for i in a:
    if i in b:
        b.append(i)
        count=count+1
if count==1:
    print("yes")
else:
    print("no")

