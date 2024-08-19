import interact
import struct

# ---- Integers ----
# ---- Unsigned Quiz Solution ----

quiz_number = 1 # unsigned

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
p.sendline(f'{quiz_number}')


p.readuntil('quiz...')
p.sendline('\n')

# --------- SKILL QUIZZ -------------

p.readuntil('bar = 0x')
data = p.read(8)
p.readuntil('\n')
print(data)
p.sendline(f'{data}')
p.readuntil('\n')

p.interactive()