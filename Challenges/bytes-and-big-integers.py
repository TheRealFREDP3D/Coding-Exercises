# -----------------------------------------------------------------------------
# Python 3.x | bytes-and-big-integers.py 
# code to demonstrate the use of bytes and big integers
# -----------------------------------------------------------------------------
# Author: Frederick Pellerin
# Twitter | X | GitHub : @TheRealFredP3D
# Website: https://link.gallery/therealfredp3d
# =============================================================================

# -----------------------------------------------------------------------------
# converting large numbers to bytes is common when working with cryptographic
# problems or applications that represent large values as sequences of bytes.
# -----------------------------------------------------------------------------
# 'to_bytes' method                            
# -----------------------------------------------------------------------------
# - provides an easy way to perform this conversion in Python.
# - returns a byte string containing the converted value.
# =============================================================================

# ----------------------------------------------------------------------------- 
# 'to_bytes' syntax
# -----------------------------------------------------------------------------
# to_bytes(length, byteorder)
#
# arguments: 
# 1. number of bytes to convert 
# 2. byte order can be 'big' or 'little'.
# -----------------------------------------------------------------------------
 
# Define a big integer
base10_msg = (
    11515195063862318899931685488813747395775516287289682636499965282714637259206269
)

# Convert the big integer to a bytes string
bytes_string = base10_msg.to_bytes(33, "big")

# Print the resulting byte string
print(f"Bytes string: {bytes_string}")
