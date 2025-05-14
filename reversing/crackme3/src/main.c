#include <stdio.h>
#include <string.h>

// Shamelessly stolen & adapted from https://github.com/NoraCodes/crackmes/blob/master/crackme01.c
// An even more less simple crackme that uses encoded string arguments instead

int main(int argc, char** argv) {

    if (argc != 2) {
        printf("Need exactly one argument.\n");
        return -1;
    }
    int correct[] = {32, 39, 86, 81, 82, 31, 60, 84, 54, 59, 85, 55, 59, 54, 87, 50, 87, 54, 55, 87, 37, 38, 40, 87, 59, 61, 84, 49, 59, 47, 42, 43, 51, 25};

    char decoded[27];
    for (int i = 0; i < 26; i++) {
        decoded[i] = (char)(correct[i]^0x64);
    }
    decoded[26] = '\0'; 
    if (strncmp(argv[1], decoded, strlen(decoded))) {
        printf("No, %s is not correct.\n", argv[1]);
        return 1;
    } else {
        printf("Yes, %s is correct!\n", argv[1]);
        return 0;
    }

}