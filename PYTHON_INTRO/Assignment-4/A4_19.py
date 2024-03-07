def is_prime2954(num2954):
    if num2954 <= 1:
        return False
    for i2954 in range(2, int(num2954**0.5) + 1):
        if num2954 % i2954 == 0:
            return False
    return True

M2954 = 10  # Example: Lower bound
N2954 = 50  # Example: Upper bound
print("Prime numbers between", M2954, "and", N2954, "are:")
for num2954 in range(M2954, N2954+1):
    if is_prime2954(num2954):
        print(num2954, end=" ")
