import math

x2954 = 2  # Example: x = 2
n2954 = 5  # Example: Sum of first 5 terms
sum2954 = 0
for i in range(n2954+1):
    sum2954 += x2954**i / math.factorial(i)
print("Sum:", sum2954)
