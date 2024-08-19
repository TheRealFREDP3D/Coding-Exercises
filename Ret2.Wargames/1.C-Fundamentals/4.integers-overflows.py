#!/bin/python2
# ============================================================================== #
# integers-overflows.py --------------------------------------------------------- # 
# ============================================================================== #
# Python 2.x.x ----------------------------------------------------------------- #
# Author: Frederick Pellerin --------------------------------------------------- #
# GitHub: https://github.com/TheRealFREDP3D ------------------------------------ #
# X:      https://twitter.com/TheRealFredP3D ----------------------------------- #
# ============================================================================== #
# ---- C Fundamentals - Integers ----
# ---- Overflows Quiz Solution ----

import interact
import struct
import re

# --- TOOLS ----

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

#  ---- SOLUTION ----

p = interact.Process()
p.readuntil('Choice:')
p.sendline('4')


p.readuntil('quiz...')
p.sendline('\n')

# ---- PROGRAM OUTPUT ----
#
# ---- SKILL QUIZ ----
# What will the following C code print?
#  
#    unsigned int bar = 64879;
#    bar -= 442094589;
#    printf("%u", bar);
#  
# Enter Answer: 

p.readuntil('int bar = ')
num_one = p.readuntil(';\n')
p.readuntil('bar -= ')
num_two = p.readuntil(';\n')

num_one = num_one.strip(b';\n')
num_two = num_two.strip(b';\n')

num_one = u64(num_one)
num_two = u64(num_two)

answer = num_one - num_two
p.sendline(str(answer))

p.interactive()