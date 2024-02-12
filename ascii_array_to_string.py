"""
|------------------------------------------------------------------------------------------------------------|
- Script Name: ascii_array_to_string.py                                                                      -
| Author: Frederick Pellerin                                                                                 |
- GitHub: https://github.com/TheRealFREDP3D                                                                  -
| Portfolio: https://link.gallery/therealfredp3d                                                             |
--------------------------------------------------------------------------------------------------------------
Description:                                                                                               |
- This script is designed to convert an array of ASCII integer values into a string. It works by iterating -
| through each integer in the provided array, converting each integer to its corresponding ASCII character   |
- using the chr() function, and concatenating these characters into a single string. The final output is     -
| the assembled character string, representing the original ASCII values in textual form.                    |
--------------------------------------------------------------------------------------------------------------
"""

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
ascii_array = [83, 116, 97, 114, 114, 121, 78, 105, 103, 104, 116, 86, 97, 110, 71, 111, 103, 104]

# Convert the ASCII integer array to a character string
result_string = ascii_array_to_string(ascii_array)

# Print the resulting string
print("Resulting String:", result_string)
