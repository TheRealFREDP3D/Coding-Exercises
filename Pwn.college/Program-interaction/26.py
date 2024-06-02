# - the challenge checks for a specific parent process : python
# - the challenge will check that input is redirected from a specific file path : /tmp/jlgpxc
# - the challenge will check for a hardcoded password over stdin : tmhhbglw

# $ python 26.py

from pwn import *
import os

try:
    # Write the string to the file
    with open("/tmp/jlgpxc", 'w') as file:
        file.write("tmhhbglw")
except Exception as e:
    print(f"Error writing to file: {e}")
    exit()

# Open the file in read-only mode and get the file descriptor
try:
    fd = os.open("/tmp/jlgpxc", os.O_RDONLY)
except Exception as e:
    print(f"Error opening file: {e}")
    exit()

# Create a process running the challenge program and pass the file descriptor as the standard input
try:
    p = process('/challenge/embryoio_level26', stdin=fd)  # replace '/path/to/your/challenge' with your actual path
except Exception as e:
    print(f"Error starting challenge: {e}")
    exit()

# Interact with the process
p.interactive()