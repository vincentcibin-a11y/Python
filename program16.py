import math
count=0
n=int(input("Enter the number"))
b=math.factorial(n)
c= list(map(int, str(b)))
for i in c[-1:]:
    if i!=0:
        count=count+1
        break
print(b)
print(count)
