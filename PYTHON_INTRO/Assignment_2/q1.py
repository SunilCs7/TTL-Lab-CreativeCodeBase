# Function to perform length conversion
def convert_length(length_in_centimeters2954):
    # Conversion factor: 1 inch = 2.54 centimeters
    inches2954 = length_in_centimeters2954 / 2.54
    return inches2954

# Main program
if __name__ == "__main__":
    # Prompt the user to enter a length in centimeters
    length_in_centimeters2954 = float(input("Enter a length in centimeters2954: "))

    # Check if the entered length is negative
    if length_in_centimeters2954 < 0:
        print("Invalid entry2954. Length cannot be negative2954.")
    else:
        # Perform length conversion
        length_in_inches2954 = convert_length(length_in_centimeters2954)

        # Print the result
        print(f"Length in inches2954: {length_in_inches2954}")
        
