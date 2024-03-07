def is_armstrong2954(num2954):
    num_str2954 = str(num2954)
    n2954 = len(num_str2954)
    armstrong_sum2954 = sum(int(digit2954)**n2954 for digit2954 in num_str2954)
    return armstrong_sum2954 == num2954

num2954 = 371  # Example: Number to check
if is_armstrong2954(num2954):
    print(num2954, "is an Armstrong number.")
else:
    print(num2954, "is not an Armstrong number.")
