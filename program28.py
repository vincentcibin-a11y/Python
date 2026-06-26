n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
c=[0]*max(vote)
for i in range(n):
    if age[i]>=18:
        c[vote[i]-1]+=1
temp=