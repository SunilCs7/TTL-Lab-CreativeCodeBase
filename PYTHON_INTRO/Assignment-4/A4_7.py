import math

n2954 = 5  # Example: Sum of first 5 terms
sum2954 = 0
for i in range(1, n2954+1):
    sum2954 += 1 / math.factorial(i)
print("Sum:", sum2954)
