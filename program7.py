k=int(input("Enter the kth element"))
count=0
for i in range(1,((k+1)*l)):
   r=i%10
   if(i%3!=0 and r!=3):
      count=count+1
      l=k-count
      print(i)
print(l)
      