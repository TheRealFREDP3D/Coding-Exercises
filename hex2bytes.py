# Define a hexadecimal string representing "Hello World"
hex_string = "48656c6c6f20576f726c64"  # Each pair of characters represents one byte in hexadecimal

# Convert the hexadecimal string to bytes using the bytes.fromhex() function
byte_data = bytes.fromhex(hex_string)

# Print the byte data
print("Byte data:", byte_data)
