# A simple program to illustrate the use of bytes and big integers

# Import the necessary module for working with big integers
import Crypto.Util.number

# Define a big integer
base10_msg = (11515195063862318899931685488813747395775516287289682636499965282714637259206269)

# Convert the big integer to a byte string
flag = base10_msg.to_bytes(33, "big")

# Print the resulting byte string
print("Flag:")
print(flag)
