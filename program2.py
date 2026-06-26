loc=int(input())
if(loc<5):
   print(1)
elif(loc%5==0):

   min=loc//5
   print(min)
else:
   min=loc//5
   print(min+1)
