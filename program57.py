a=input("Enter a string")
count=0
for i in a:
    if i in "aeiou":
        count=count+1
print(count)