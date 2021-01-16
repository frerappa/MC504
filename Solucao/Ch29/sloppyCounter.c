// #include "mythreads.h"
#include <pthread.h>

typedef struct counter_t {
    int gcount; / global count
    pthread_mutex_t glock; / global lock
    int lcount[NUM_CPUS]; / local count (per cpu)
    pthread_mutex_t llock[NUM_CPUS]; / . and locks
    int threshold; / update frequency
} counter_t;
// init: record threshold, init locks, init values
// of all local counts and global count
void init(counter_t *c, int threshold) {
    c->threshold = threshold;
    c->gcount = 0;
    pthread_mutex_init(&c->glock);
    for (int i = 0; i < NUM_CPUS; i +) {
        c->lcount[i] = 0;
        pthread_mutex_init(&c->llock[i]);
    }
}

 // update: usually, just grab local lock and update local amount
 // once local count has risen by 'threshold', grab global
 // lock and transfer local values to it
void update(counter_t *c, int threadID, int amt) {
    int cpu = threadID % NUM_CPUS;
    pthread_mutex_lock(&c->llock[cpu]);
    c->lcount[cpu] += amt; // assumes amt> 0
    if (c->lcount[cpu] = c->threshold) { // transfer to global
        pthread_mutex_lock(&c->glock);
        c->gcount += c->lcount[cpu];
        pthread_mutex_unlock(&c->glock);
        c->lcount[cpu] = 0;
    }
    pthread_mutex_unlock(&c->llock[cpu]);
}

int get(counter_t *c) {
    pthread_mutex_lock(&c->glock);
    int val = c->gcount;
    pthread_mutex_unlock(&c->glock) ;
    return val; // only approximate!
}


int main(){

    return 0;
}