l=[1,2,3,4,5,6,7]
k=int(input("Enter the k values"))
n=len(l)
k=k%n
def reverse(i,j):
    while i<j:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
reverse(0,k-1)
reverse(k,n-1)
reverse(0,n-1)
print(l)