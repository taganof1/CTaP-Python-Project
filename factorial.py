import math

def fac(n):
    return(math.factorial(n))

num = int(input("Enter a Number: "))
f = fac(num)
print("Factorial of", num, "is", f)

