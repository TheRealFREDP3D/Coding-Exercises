from pwn import *

io = process(['/challenge/embryoio_level18', '<', '/tmp/xwiaeb'])
print(io.recvall())