from pwn import *
import os

"""
This script is used to solve the Program Interaction Level 20 challenge.

The challenge checks for a specific parent process : ipython
The challenge will check that output is redirected to a specific file path : /tmp/yjcqvm
"""

# Open the file in write-only mode and get the file descriptor
fd = os.open('/tmp/yjcqvm', os.O_WRONLY | os.O_CREAT)

# Create a process running the challenge program and pass the file
# descriptor as the standard output
p = process("/challenge/embryoio_level20", stdout=fd)

# Read the contents of the file
with open('/tmp/yjcqvm', 'r') as file:
    print(file.read())

# Interact with the process
p.interactive()

