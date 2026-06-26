def fun(n):
  if n==0:
    return 0
  elif n%2==0:
    return 1+fun(n//2)
  else:
    return 1+fun((n-1)//2)
n=int(input("Enter a number"))
print(fun(n))

