import math
n=int(input("Enter the number"))
flag=0
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        flag=flag+1
        break
if flag==0:
    print("Prime")
else:
    print("Not prime")