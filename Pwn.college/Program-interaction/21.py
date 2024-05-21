# - the challenge checks for a specific parent process : ipython
# - the challenge will check that the environment is empty (except LC_CTYPE, which is impossible to get rid of in some cases)

from pwn import *
import os

p = process("/challenge/embryoio_level21", env={})

p.interactive()
