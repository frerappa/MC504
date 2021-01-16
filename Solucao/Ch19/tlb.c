#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>    

int main(int argc, char *argv[]){

    if (argc == 3){
        for (int pg = 2; pg <= 16384; pg*=2){
            int NUMPAGES = pg, PAGESIZE = 1048576/*1048576*/;
            long int NUMTRIALS = atoi(argv[2]);
            int jump = PAGESIZE / sizeof(int);
            int size = (int) (NUMPAGES * jump);
            int *a;
            a = (int*) malloc((unsigned long int) NUMPAGES * jump * sizeof(int));
            struct timespec start, end;
            double tempo_de_acesso;
            long int counter = 1; 
            timespec_get(&start, TIME_UTC);
            while (counter <= NUMTRIALS){
                for (unsigned long int i = 0; i < NUMPAGES * jump; i += jump){
                    a[i] += 1;
                }
                counter++;
            }
            timespec_get(&end, TIME_UTC);
            long int nanoseconds = (end.tv_sec - start.tv_sec)*1000000000 + (end.tv_nsec - start.tv_nsec);
            tempo_de_acesso = ((double) nanoseconds) / ((unsigned long int) NUMTRIALS*NUMPAGES);
            printf("%d                          %.5f ns\n", pg, tempo_de_acesso);
            free(a);
        }
    }
    return 0;
}