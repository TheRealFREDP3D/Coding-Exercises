# ============================================================================= #
# bytes-and-big-integers.py --------------------------------------------------- #
# ============================================================================= #
# Python 3.x.x ---------------------------------------------------------------- #
# Author: Frederick Pellerin -------------------------------------------------- #
# GitHub: https://github.com/TheRealFREDP3D ----------------------------------- #
# Twitter: https://twitter.com/TheRealFredP3D --------------------------------- #
# ============================================================================= #
# Converting large numbers to bytes is common when working with cryptographic - #
# problems or applications that represent large values as sequences of bytes. - #
# ============================================================================= #
# to_bytes(length, byteorder) ------------------------------------------------- #
# length: Number of bytes to convert ------------------------------------------ #
# byteorder: Can be 'big' or 'little'.----------------------------------------- #
# ============================================================================= #

# Define a big integer
base10_msg = (
    11515195063862318899931685488813747395775516287289682636499965282714637259206269
)

# Convert the big integer to a bytes string
bytes_string = base10_msg.to_bytes(33, 'big')

# Print the resulting byte string
print(f'Bytes string: {bytes_string}')
