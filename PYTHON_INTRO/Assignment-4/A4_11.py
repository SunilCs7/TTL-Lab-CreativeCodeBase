num2954 = 7  # Example: Number to check
if num2954 > 1:
    for i in range(2, int(num2954/2) + 1):
        if (num2954 % i) == 0:
            print(num2954, "is composite.")
            break
    else:
        print(num2954, "is prime.")
else:
    print(num2954, "is neither prime nor composite.")
