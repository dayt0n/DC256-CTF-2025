#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <sys/types.h>
#include <unistd.h>


void storeFlag(char* flag) {
    FILE* flagFile = fopen("flag.txt", "r");
    if (flagFile == NULL) {
        printf("Flag file not found.\n");
        return;
    }
    fgets(flag, 64, flagFile);
}

int truemain() {
    char flag[64] = {0};
    char input[64] = {0};
    storeFlag(flag);

    scanf("%63[^\n]", input);
    printf("You have input: ");
    printf(input);

    if (!strncmp(input, "supersecretpassword", strlen("supersecretpassword"))) {
        printf("Yay password! It still wont be that easy :)");
    } else {
        printf("It wont be that easy...");
    }
    return 1;
}

int main(){
    setvbuf(stdout, NULL, _IONBF,  0);

    printf("Please input the correct password: ");
    truemain();
}