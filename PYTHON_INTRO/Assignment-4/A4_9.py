import math

x2954 = 1  # Example: x = 1
n2954 = 5  # Example: Number of terms
sin_x2954 = 0
for i in range(n2954+1):
    sin_x2954 += ((-1)**i * x2954**(2*i + 1)) / math.factorial(2*i + 1)
print("sin(x):", sin_x2954)
