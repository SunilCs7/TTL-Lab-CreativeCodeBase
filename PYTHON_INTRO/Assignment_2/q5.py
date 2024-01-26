# Get user input
num_items2954 = int(input("Enter the number of items: "))

# Calculate total cost
if num_items2954 < 10:
    total_cost2954 = num_items2954 * 12
elif 10 <= num_items2954 < 100:
    total_cost2954 = num_items2954 * 10
else:
    total_cost2954 = num_items2954 * 7

print(f"Total cost2954: ${total_cost2954}")
