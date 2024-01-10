# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Swap values
num1, num2, num3 = num2, num3, num1

print(
    f"After swapping:\nFirst number: {num1}\nSecond number: {num2}\nThird number: {num3}"
)
