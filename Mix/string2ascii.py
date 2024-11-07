# Define a function called string_to_ascii that takes an input_string as parameter
def string_to_ascii(input_string):

    # Create an empty list to store the ASCII codes
    ascii_list = []

    # Iterate through each character in the input_string
    for char in input_string:

        # Convert the character to its ASCII code using the ord() function
        ascii_code = ord(char)

        # Add the ASCII code to the ascii_list
        ascii_list.append(ascii_code)

    # Return the list of ASCII codes
    return ascii_list

# Prompt the user to enter a string and store it in the variable input_string
input_string = input('Enter a string: ')

# Call the string_to_ascii function with the input_string as argument and store the result in ascii_codes
ascii_codes = string_to_ascii(input_string)

# Print a message indicating the purpose of the output
print('ASCII codes for each character in the input string:')

# Iterate through each ASCII code in the ascii_codes list
for code in ascii_codes:

    # Print each ASCII code
    print(code)
