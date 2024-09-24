# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Call the function with a sample number
result = factorial(5)

# Print the result
print("Factorial:", result)
