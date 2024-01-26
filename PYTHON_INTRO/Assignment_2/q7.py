# Get user input
year2954 = int(input("Enter a year2954: "))

# Check if it is a leap year
if (year2954 % 4 == 0 and year2954 % 100 != 0) or (year2954 % 400 == 0):
    print(f"{year2954} is a leap year2954.")
else:
    print(f"{year2954} is not a leap year2954.")
