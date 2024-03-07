def fibonacci2954(n2954):
    fib_series2954 = [0, 1]
    for i2954 in range(2, n2954):
        fib_series2954.append(fib_series2954[i2954-1] + fib_series2954[i2954-2])
    return fib_series2954

n2954 = 10  # Example: Number of terms in Fibonacci series
print("Fibonacci series up to", n2954, "terms:", fibonacci2954(n2954))


