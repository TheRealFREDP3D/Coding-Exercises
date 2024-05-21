# - the challenge checks for a specific parent process : python
# - the challenge will check for a hardcoded password over stdin : pfugoklk

# $ python 23.py

from pwn import *

p = process("/challenge/embryoio_level23")
p.stdin.write(b'pfugoklk\n')
p.stdin.flush()

p.interactive()

