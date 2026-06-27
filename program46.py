a=[]
s="ab##"
s1=list(s)
t="a#d#"
t1=list(t)
for i in s1:
    if i=="#":
        while(i!='#'):
            s1.pop(s1.index("#")-1)
            i=i-1
for j in t1:
    if j=="#":
        while(j!="#"):
            t1.pop(t1.index("#")-1)
            i=i-1
if s1==t1:
    print("true")
else:
    print("false")


