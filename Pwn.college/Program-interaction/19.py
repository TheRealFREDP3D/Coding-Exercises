#!/bin/python3


# /tmp/xwiaeb
# bvfrxxiy


from pwn import *
import os

"""
This script is used to solve the Program Interaction Level 19 challenge.

The challenge is to open a file and pass the file descriptor to a process
running the challenge program. The file descriptor is then used by the
program to read the contents of the file.
"""

# Write the string to the file
with open("/tmp/xwiaeb", 'w') as file:
    file.write("tmhhbglw")

# Open the file in read-only mode and get the file descriptor
fd = os.open("/tmp/xwiaeb", os.O_RDONLY)

# Create a process running the challenge program and pass the file
# descriptor as the standard input
p = process('/challenge/embryoio_level19', stdin=fd)

# Interact with the process
p.interactive()

