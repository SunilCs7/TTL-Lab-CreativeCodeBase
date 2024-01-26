# Get user input for the height of the diamond
diamond_height2954 = int(input("Enter the height of the diamond: "))

# Print the diamond
for i in range(1, diamond_height2954 + 1):
    print(' ' * (diamond_height2954 - i) + '*' * (2 * i - 1))

for i in range(diamond_height2954 - 1, 0, -1):
    print(' ' * (diamond_height2954 - i) + '*' * (2 * i - 1))
