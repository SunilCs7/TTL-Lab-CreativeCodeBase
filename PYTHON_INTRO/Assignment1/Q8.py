import math

# Input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter
area = math.pi * radius**2
perimeter = 2 * math.pi * radius

print(f"Area of the circle: {area:.2f}\nPerimeter of the circle: {perimeter:.2f}")
