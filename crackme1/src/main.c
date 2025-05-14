#include <stdio.h>
#include <string.h>

// Shamelessly stolen from https://github.com/NoraCodes/crackmes/blob/master/crackme01.c
// A very simple crackme which stores the correct password in program memory

int main(int argc, char** argv) {

    if (argc != 2) {
        printf("Need exactly one argument.\n");
        return -1;
    }

    char* correct = "DC256{th1s_sh0uld_b3_eZ_wiTH_str1ngz}";

    if (strncmp(argv[1], correct, strlen(correct))) {
        printf("No, %s is not correct.\n", argv[1]);
        return 1;
    } else {
        printf("Yes, %s is correct!\n", argv[1]);
        return 0;
    }

}