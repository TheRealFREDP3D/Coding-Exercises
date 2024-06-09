from pwn import xor  # Import the xor function from the pwn module

# Define the encrypted string in hexadecimal format
crypted_str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# Perform the XOR operation with the first byte of the string and the ASCII value of the character 'c'
key = xor(crypted_str[0], ord('c'))

# Print the result of the XOR operation
print(xor(crypted_str, key))
