def generate_fibonacci2954(n):
    fib_sequence2954 = [0, 1]

    while fib_sequence2954[-1] + fib_sequence2954[-2] <= n:
        fib_sequence2954.append(fib_sequence2954[-1] + fib_sequence2954[-2])

    return fib_sequence2954

# Get user input for N
N2954 = int(input("Enter a value for N: "))

# Generate and print the Fibonacci sequence up to N
result2954 = generate_fibonacci2954(N2954)
print("Fibonacci Sequence up to N2954:", result2954)
