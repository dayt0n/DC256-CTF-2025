#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    system("echo executing...");
#define BINSH "/bin/bash"
    printf("doing %s\n", BINSH);
    __asm__(
        "movq $0x00402016, %rdi;"
        "movq $0x04011ed, %rax;"
        "jmp %rax;");
    return 0;
}