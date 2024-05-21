# - the challenge checks for a specific parent process : python
# $ python 22.py

from pwn import *

p = process("/challenge/embryoio_level22")
p.interactive()
