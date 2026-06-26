d=int(input("Enter the digit"))
n=d
s=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
print(s)