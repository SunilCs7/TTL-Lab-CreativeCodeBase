# Get user input for the width and height of the box
width2954 = int(input("Enter the width of the box: "))
height2954 = int(input("Enter the height of the box: "))

# Print the custom box
for i in range(height2954):
    if i == 0 or i == height2954 - 1:
        print('*' * width2954)
    else:
        print('*' + ' ' * (width2954 - 2) + '*')
