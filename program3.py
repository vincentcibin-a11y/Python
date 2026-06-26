a,b=map(int,input().split())
count=0
if(a<=10 and b<=10):
  while(a<=b):
    a=a*3
    b=b*2
    count=count+1
print(count)