def alternate_case_characters(string):
    result = ''
    for i, char in enumerate(string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(string):
    words = string.split()
    result = ''
    for i, word in enumerate(words):
        if i % 2 == 0:
            result += word.lower()
        else:
            result += word.upper()
        result += ' '
    return result.strip()

# Read input string from user
input_string = input("Enter a string: ")

# Making alternate characters upper and lower case
alternate_characters_result = alternate_case_characters(input_string)
print("Alternate case characters result:", alternate_characters_result)

# Making alternate words lower and upper case
alternate_words_result = alternate_case_words(input_string)
print("Alternate case words result:", alternate_words_result)
