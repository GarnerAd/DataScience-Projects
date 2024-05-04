# Read the times (in minutes) for swimming, cycling, and running
swim_time = int(input("Enter the swimming time (in minutes): "))
cycle_time = int(input("Enter the cycling time (in minutes): "))
run_time = int(input("Enter the running time (in minutes): "))

# Calculate the total time taken to complete the triathlon
total_time = swim_time + cycle_time + run_time

# Determine the award based on the total time
if total_time <= 100:
    award = "Provincial colours"
elif total_time <= 105:
    award = "Provincial half colours"
elif total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

# Display the award the participant will receive
print("The award the participant will receive is:", award)
