# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swap values without using a third variable
num1, num2 = num2, num1

print(f"After swapping: \nFirst number: {num1}\nSecond number: {num2}")
