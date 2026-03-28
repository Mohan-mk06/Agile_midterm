
n = int(input("Enter number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
    exit(1)
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "is", fact)

n=int(input("Enter number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)
