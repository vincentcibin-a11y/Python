s="   fly me   to   the moon  "
a=s.split(" ")
count=0
for i in a[-1:]:
    if len(i)==0:
        count=count+1
print(a[count+1])
print(count)
