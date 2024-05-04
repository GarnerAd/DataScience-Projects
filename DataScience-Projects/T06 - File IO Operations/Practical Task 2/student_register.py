# Ask the user for the number of students registering
num_students = int(input("How many students are registering? "))

# Open the file in write mode
with open('reg_form.txt', 'w') as file:
    # Iterate for the number of students entered by the user
    for i in range(num_students):
        # Ask the user to enter the student ID number
        student_id = input(f"Enter student ID for student {i+1}: ")
        # Write the student ID number to the file
        file.write(student_id + '\n')
        # Write a dotted line as per the requirement
        file.write("-" * len(student_id) + '\n')

print("Registration complete. Please check reg_form.txt for the attendance register.")
