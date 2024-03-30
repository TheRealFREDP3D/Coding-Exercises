# bytes-and-big-integers.py
# Python 3.x code to demonstrate the use of bytes and big integers
# -------------------------------------------------------------------------------------------
# Created by: Frederick Pellerin
# Twitter: @TheRealFredP3D
# Website: https://link.gallery/therealfredp3d
# -------------------------------------------------------------------------------------------
# Converting large numbers to bytes in this way is common when working with cryptographic
# problems or other applications that need to represent large values as sequences of bytes.
# The 'to_bytes' method provides an easy way to perform this conversion in Python.
# The 'to_bytes' method takes two arguments: the number of bytes to convert to and the
# byte order. The byte order can be either 'big' or 'little'.
# The 'to_bytes' method returns a byte string containing the converted value.
# ------------------------------------------------------------------------------------------- 

# Define a big integer
base10_msg = (
    11515195063862318899931685488813747395775516287289682636499965282714637259206269
)

# Convert the big integer to a byte string
flag = base10_msg.to_bytes(33, "big")

# Print the resulting byte string
print(f"Flag: {flag}")
