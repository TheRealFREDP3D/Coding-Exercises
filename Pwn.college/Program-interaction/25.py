# - the challenge checks for a specific parent process : python
# - the challenge will check that env[KEY] holds value VALUE (listed to the right as KEY:VALUE) : fimoun:shspjejaxc

# $ python 25.py

from pwn import *

p = process(["/challenge/embryoio_level25"], env={"fimoun": "shspjejaxc"})

p.interactive()