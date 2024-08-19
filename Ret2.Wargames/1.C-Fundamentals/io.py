import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
p.readuntil('3. Quit')
p.sendline('1') 

p.readuntil('data:')
p.sendline('blablabla')

p.readuntil('quiz...')
p.sendline('\n')

p.readuntil('Answer:')
p.sendline('Hello\nWorld!\n\xC0\xDE\xF0\x0D')
p.interactive()