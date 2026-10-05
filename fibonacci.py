def fibonacci_loop(n):
    """Generates a list containing the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the first two terms
    sequence = [0, 1]
    
    # Dynamically calculate the remaining terms
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
        
    return sequence

# Example usage: Generate the first 10 numbers
print(fibonacci_loop(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
