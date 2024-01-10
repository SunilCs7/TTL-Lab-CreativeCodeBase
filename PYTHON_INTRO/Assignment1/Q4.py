# Input basic salary
basic_salary = float(input("Enter basic salary: "))

# Calculate TA, DA, HRA, and Gross
ta = 0.2 * basic_salary
da = 1.2 * basic_salary
hra = 0.3 * basic_salary
gross_salary = basic_salary + ta + da + hra

print(f"TA: {ta:.2f}\nDA: {da:.2f}\nHRA: {hra:.2f}\nGross Salary: {gross_salary:.2f}")
