# Initialize variables
total = 0
count = 0

# Continuously ask the user to enter a number
while True:
    num = input("Enter a number (enter -1 to stop): ")

    # Check if the input is -1 to stop the loop
    if num == "-1":
        break

    # Convert the input to an integer and add it to the total
    num = int(num)
    total += num
    count += 1

# Calculate the average if at least one number was entered
if count > 0:
    average = total / count
    print("Average of the numbers entered (excluding -1):", average)
else:
    print("No numbers were entered.")