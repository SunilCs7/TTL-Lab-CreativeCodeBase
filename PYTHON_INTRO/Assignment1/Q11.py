# Input the sides of the triangle
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))

# Calculate the semi-perimeter
s = (side_a + side_b + side_c) / 2

# Calculate the area using Heron's formula
area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5

print(f"Area of the triangle: {area:.2f}")
