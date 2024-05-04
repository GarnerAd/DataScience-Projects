# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate the sum of all three numbers
sum_of_numbers = num1 + num2 + num3
print("The sum of all the numbers:", sum_of_numbers)

# Calculate the difference between the first and second numbers
difference_first_second = num1 - num2
print("The first number minus the second number:", difference_first_second)

# Calculate the product of the third number and the first number
product_third_first = num3 * num1
print("The third number multiplied by the first number:", product_third_first)

# Calculate the sum of all three numbers divided by the third number
sum_divided_by_third = sum_of_numbers / num3
print("The sum of all three numbers divided by the third number:", sum_divided_by_third)