#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h> 
#include <sys/types.h>
#include <unistd.h>

void printFlag() {
    FILE* flagFile = fopen("flag.txt", "r");
    char* flag[64] = {0};
    if (flagFile == NULL) {
        printf("Flag file not found.\n");
        return;
    }
    fgets(flag, 64, flagFile);
    printf("%s\n", flag);
}

int truemain() {
    char input[64];

    gets(input);
    puts(input);

    if (strncmp(input, "supersecretpassword", strlen("supersecretpassword"))) {
        return 1;
    } else {
        return 0;
    }

}

int main(){
    setvbuf(stdout, NULL, _IONBF,  0);

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    printf("Please input password: ");
    truemain();
}