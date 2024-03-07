m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

for num in range(m, n + 1, 2):  # Increment by 2 to print odd numbers
    print(num)
