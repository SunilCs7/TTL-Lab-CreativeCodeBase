# Input principal amount, rate of interest, and time
principal = float(input("Enter principal amount: "))
rate_of_interest = float(input("Enter rate of interest (in percentage): "))
time = float(input("Enter time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate_of_interest * time) / 100

# Calculate Compound Interest
compound_interest = principal * (1 + rate_of_interest / 100) ** time - principal

print(
    f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
)
