# Get user input
temperature_in_celsius2954 = float(input("Enter a temperature in Celsius2954: "))

# Temperature classification
if temperature_in_celsius2954 < -273.15:
    print("Invalid temperature2954. It is below absolute zero2954.")
elif temperature_in_celsius2954 == -273.15:
    print("Absolute Zero2954.")
elif -273.15 < temperature_in_celsius2954 < 0:
    print("Temperature is below freezing2954.")
elif temperature_in_celsius2954 == 0:
    print("Temperature is at freezing point2954.")
elif 0 < temperature_in_celsius2954 <= 100:
    print("Temperature is in the normal range2954.")
elif temperature_in_celsius2954 == 100:
    print("Temperature is at boiling point2954.")
else:
    print("Temperature is above boiling point2954.")
