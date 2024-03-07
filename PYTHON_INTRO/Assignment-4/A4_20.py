def gcd2954(a2954, b2954):
    while b2954:
        a2954, b2954 = b2954, a2954 % b2954
    return a2954

def is_relatively_prime2954(num2954, other2954):
    return gcd2954(num2954, other2954) == 1

num2954 = 10  # Example: Number
print("Positive numbers less than", num2954, "and relatively prime to", num2954, "are:")
for i2954 in range(1, num2954):
    if is_relatively_prime2954(num2954, i2954):
        print(i2954, end=" ")
