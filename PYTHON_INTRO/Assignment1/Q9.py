# Input marks in 5 subjects
marks_subject1 = float(input("Enter marks for subject 1: "))
marks_subject2 = float(input("Enter marks for subject 2: "))
marks_subject3 = float(input("Enter marks for subject 3: "))
marks_subject4 = float(input("Enter marks for subject 4: "))
marks_subject5 = float(input("Enter marks for subject 5: "))

# Calculate average
average_marks = (
    marks_subject1 + marks_subject2 + marks_subject3 + marks_subject4 + marks_subject5
) / 5

print(f"Average marks: {average_marks:.2f}")
