#include <time.h>
#include <sys/time.h>
#include <stdio.h>

int main(){
    
    clock_t start, end;
    double cpu_time_used;
    int ITERATIONS = 10000;
    start = clock();
    for (int i = 0; i < ITERATIONS; i++){
        struct timeval current_time;
        gettimeofday(&current_time, NULL);
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / (CLOCKS_PER_SEC);
    printf("Tempo por chamada de syscall: %.10f s\n", cpu_time_used/ITERATIONS);
    return 0;
}