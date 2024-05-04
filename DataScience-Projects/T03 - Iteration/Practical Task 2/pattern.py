# Define the number of rows in the pattern
rows = 9

# Loop through each row
for i in range(1, rows + 1):
    # If the row is less than or equal to 5, print increasing number of asterisks
    if i <= 5:
        print("*" * i)
    # If the row is greater than 5, print decreasing number of asterisks
    else:
        print("*" * (rows - i))
