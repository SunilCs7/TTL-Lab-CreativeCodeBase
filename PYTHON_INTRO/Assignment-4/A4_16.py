def is_palindrome2954(num2954):
    return str(num2954) == str(num2954)[::-1]

num2954 = 12321  # Example: Number to check
if is_palindrome2954(num2954):
    print(num2954, "is a palindrome.")
else:
    print(num2954, "is not a palindrome.")
