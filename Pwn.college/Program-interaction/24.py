# - the challenge checks for a specific parent process : python
# - the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 1:urbjnyuygs

# python 24.py

from pwn import *

p = process(["/challenge/embryoio_level24", "urbjnyuygs"])

p.interactive()