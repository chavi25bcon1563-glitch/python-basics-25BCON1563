def factorial_loop(n):
    # Factorial is not defined for negative numbers
    if n < 0:
        return "Factorial is not defined for negative numbers."
    # The factorial of 0 and 1 is always 1
    elif n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
num = 5
print(f"The factorial of {num} is {factorial_loop(num)}")
# Output: The factorial of 5 is 120

