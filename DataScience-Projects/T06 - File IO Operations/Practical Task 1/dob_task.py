# Open and read the data from the text file
with open('DOB.txt', 'r') as file:
    data = file.readlines()

# Initialize lists to store names and birthdates
names = []
birthdates = []

# Extract names and birthdates from the data
for line in data:
    parts = line.strip().split(' ')
    names.append(' '.join(parts[:-3]))
    birthdates.append(' '.join(parts[-3:]))

# Print out the names section
print("Name")
print("\n".join(names))
print()

# Print out the birthdates section
print("Birthdate")
print("\n".join(birthdates))
