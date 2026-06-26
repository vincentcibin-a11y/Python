def fun(n,m=0):
    if m==n:
        return 
    print(m+1,end=" ")
    fun(n,m+1)
    print(m+1,end=" ")
n=5
fun(n)