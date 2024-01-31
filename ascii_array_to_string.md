---
title: ASCII Code to Character
tags: ascii, char, character, code, python, chr(), convert, ord()
reference: https://cryptohack.org/courses/intro/enc1/
type: code/python
---

# ascii2char.py

- ASCII is a 7-bit encoding standard
- Representation of text using the integers 0-127.

---

## Python Application

### chr() Function 

chr() function can convert *ASCII ordinal number* to *character*.

---

### ord() Function 

ord() function can convert *character* to *ASCII ordinal number*.

---

## Examples 
```python

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


# Define an ASCII integer array
ascii_array = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]

# Convert the ASCII integer array to a character string
result_string = ascii_array_to_string(ascii_array)

# Print the resulting string
print("Resulting String:", result_string)

