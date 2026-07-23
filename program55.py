a=int(input("Enter number to search:"))
b=[]
for i in range(0,5):
      b.append(int(input("Enter elements")))
if a in b:
    print(b.index(a))
