flag = "DC256{H0P3_Y0U_BR0UGHT_Y0UR_R3V3RSE_ENG1N33R_H4T}"
chars = ", ".join([str(ord(char)) for char in flag])

with open("main.c", "w") as f:
    f.truncate(0)
    f.write("""
#include <stdio.h>
#include <string.h>

// Shamelessly stolen & adapted from https://github.com/NoraCodes/crackmes/blob/master/crackme01.c
// A less simple crackme that uses encoded string arguments instead

int main(int argc, char** argv) {

    if (argc != 2) {
        printf("Need exactly one argument.\\n");
        return -1;
    }
    int correct[] = {""")


    f.write(chars + "};\n")

    f.write("""
    char decoded[44];
    for (int i = 0; i < 43; i++) {
        decoded[i] = (char)correct[i];
    }
    decoded[43] = '\\0'; 
    if (strncmp(argv[1], decoded, strlen(decoded))) {
        printf("No, %s is not correct.\\n", argv[1]);
        return 1;
    } else {
        printf("Yes, %s is correct!\\n", argv[1]);
        return 0;
    }

}""")
