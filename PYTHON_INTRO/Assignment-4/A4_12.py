def gcd2954(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm2954(a, b):
    return (a * b) // gcd2954(a, b)

num12954 = 12  # Example: First number
num22954 = 18  # Example: Second number
print("GCD:", gcd2954(num12954, num22954))
print("LCM:", lcm2954(num12954, num22954))
