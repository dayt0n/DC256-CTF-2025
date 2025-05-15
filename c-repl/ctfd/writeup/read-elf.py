from pwn import *

#p = process("../target/debug/c-repl")
p = remote('127.0.0.1', 59678)
p.recvuntil("C> ")
p.sendline('#define BINSH "/bin/bash"')
p.recvuntil("C> ")
p.sendline('printf("%s",BINSH);')
data = bytes(
    [int(x, 16) for x in p.recvline().decode().split(": [")[1].strip()[:-1].split(", ")]
)

with open("elf.bin", "wb") as fp:
    fp.write(data)