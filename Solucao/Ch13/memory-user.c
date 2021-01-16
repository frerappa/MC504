#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// #include <sys/types.h>
// #include <unistd.h>

int main(int argc, char *argv[]){
    if (argc == 2){
        int mb = atoi(argv[1]);
        int n_elem = (mb*1000000)/4;
        int *v;
        v = malloc(mb*1000000);
        for (int i = 0; i < n_elem; i++){
            v[i] = i;
            if (i == n_elem - 1){
                i = 0;
            }
        }
    }
    else{
        printf("E necessario indicar o numero de MB utilizados\n");
    }
    return 0;
}