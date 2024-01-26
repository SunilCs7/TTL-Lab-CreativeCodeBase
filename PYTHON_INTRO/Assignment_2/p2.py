def convert_temperature(temp, unit2954):
    if unit2954 == 'C':
        return 9/5 * temp + 32
    elif unit2954 == 'F':
        return 5/9 * (temp - 32)

# Get user input
temperature2954 = float(input("Enter a temperature: "))
unit2954 = input("Enter the unit (C/F): ")

# Perform conversion
converted_temperature2954 = convert_temperature(temperature2954, unit2954)

print(f"Converted temperature2954: {converted_temperature2954} in the other unit2954")
