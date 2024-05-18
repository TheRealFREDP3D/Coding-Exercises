# $ ipython

from pwn import *

io = process(['/challenge/embryoio_level17', 'ztbkohtbhr'])

print(io.recvall())