#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>    
#include <sys/time.h>    

int main(int argc){
    struct timeval start1, end1, temp1;
    struct timespec temp2;
    gettimeofday(&start1, NULL);
    int iterations = 10000000;
    for (int pg = 0; pg < iterations; pg++){
        gettimeofday(&temp1, NULL);
    }
    gettimeofday(&end1, NULL);
    printf("gettimeofday: %f us\n",  (float) (1000000/iterations)*(end1.tv_sec - start1.tv_sec) + (float) (end1.tv_usec - start1.tv_usec)/iterations);
    gettimeofday(&start1, NULL);
    for (int pg = 0; pg < iterations; pg++){
        timespec_get(&temp2, TIME_UTC);
    }
    gettimeofday(&end1, NULL);
    printf("timespec_get: %f us\n", (float) (1000000/iterations)*(end1.tv_sec - start1.tv_sec) + (float) (end1.tv_usec - start1.tv_usec)/iterations);
    return 0;
}