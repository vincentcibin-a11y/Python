try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    print(a//b)
except ZeroDivisionError:
    print("Division by zero is not possible")
finally:
    print("a")


        
    