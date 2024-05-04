# Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

# Calculate and display the length of str_manip
print("Length of str_manip:", len(str_manip))

# Find the last letter in str_manip sentence and replace every occurrence of this letter with '@'
last_letter = str_manip[-1]
str_manip_replaced = str_manip.replace(last_letter, '@')

# Print the modified sentence
print("Modified sentence:", str_manip_replaced)

# Print the last three characters of str_manip backwards
print("Last three characters backwards:", str_manip[-1:-4:-1])

# Create a five-letter word made up of the first three characters and the last two characters in str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]

# Print the five-letter word
print("Five-letter word:", five_letter_word)
