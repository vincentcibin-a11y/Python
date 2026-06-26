a=input("Enter list with space separated")
b=list(a.split())
c=[]
for d in b:
    if d not in c and b.count(d)%2!=0:
        c.append(d)
print(c)

    