def factorial(n):
    # Base case
    if (n == 0 or n == 1):
        return 1;
    # else: 
    # Solve one case Baki Recursion dekh lega
    return n * factorial(n-1) #Recursive call

print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))

