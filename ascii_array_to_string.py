def ascii_array_to_string(ascii_array):
    # Initialize an empty string to store the converted characters
    char_string = ""
    
    # Iterate through each integer in the ASCII array
    for ascii_val in ascii_array:
        # Convert the ASCII integer to its corresponding character using chr() function
        char = chr(ascii_val)
        # Append the character to the string
        char_string += char
    
    # Return the resulting character string
    return char_string

# Example usage:
# Define an ASCII integer array
ascii_array = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]

# Convert the ASCII integer array to a character string
result_string = ascii_array_to_string(ascii_array)

# Print the resulting string
print("Resulting String:", result_string)
