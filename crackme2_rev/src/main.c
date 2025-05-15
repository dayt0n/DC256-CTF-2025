
#include <stdio.h>
#include <string.h>

// Shamelessly stolen & adapted from https://github.com/NoraCodes/crackmes/blob/master/crackme01.c
// A less simple crackme that uses encoded string arguments instead

int main(int argc, char** argv) {

    if (argc != 2) {
        printf("Need exactly one argument.\n");
        return -1;
    }
    int correct[] = {68, 67, 50, 53, 54, 123, 72, 48, 80, 51, 95, 89, 48, 85, 95, 66, 82, 48, 85, 71, 72, 84, 95, 89, 48, 85, 82, 95, 82, 51, 86, 51, 82, 83, 69, 95, 69, 78, 71, 49, 78, 51, 51, 82, 95, 72, 52, 84, 125};

    char decoded[44];
    for (int i = 0; i < 43; i++) {
        decoded[i] = (char)correct[i];
    }
    decoded[43] = '\0'; 
    if (strncmp(argv[1], decoded, strlen(decoded))) {
        printf("No, %s is not correct.\n", argv[1]);
        return 1;
    } else {
        printf("Yes, %s is correct!\n", argv[1]);
        return 0;
    }

}