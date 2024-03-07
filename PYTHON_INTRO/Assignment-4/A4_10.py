import math

x2954 = 1  # Example: x = 1
n2954 = 5  # Example: Number of terms
cos_x2954 = 0
for i in range(n2954+1):
    cos_x2954 += ((-1)**i * x2954**(2*i)) / math.factorial(2*i)
print("cos(x):", cos_x2954)
