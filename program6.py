n,k=map(int,input().split())
for i in range(1,k+1):
    r=n%10
    if r!=0:
        n=n-1
    elif r==0:
        n=n//10
print(n)