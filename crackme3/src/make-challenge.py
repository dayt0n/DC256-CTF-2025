flag = "DC256{X0R_1S_R3V3RS3ABL3_Y0U_KNOW}"
chars = ", ".join([str(ord(char)^0x64) for char in flag])

with open("main.c", "w") as f:
    f.truncate(0)
    f.write("""\
#include <stdio.h>
#include <string.h>

// Shamelessly stolen & adapted from https://github.com/NoraCodes/crackmes/blob/master/crackme01.c
// An even more less simple crackme that uses encoded string arguments instead

int main(int argc, char** argv) {

    if (argc != 2) {
        printf("Need exactly one argument.\\n");
        return -1;
    }
    int correct[] = {""")

    f.write(chars + "};\n")

    f.write("""
    char decoded[27];
    for (int i = 0; i < 26; i++) {
        decoded[i] = (char)(correct[i]^0x64);
    }
    decoded[26] = '\\0'; 
    if (strncmp(argv[1], decoded, strlen(decoded))) {
        printf("No, %s is not correct.\\n", argv[1]);
        return 1;
    } else {
        printf("Yes, %s is correct!\\n", argv[1]);
        return 0;
    }

}""")