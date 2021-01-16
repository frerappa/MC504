# Respostas:

## Código  

### Questão 1
O código é:
```c
void *child(void *arg) {
    printf("child\n");
    Sem_post(&s);
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t p;
    printf("parent: begin\n");
    Sem_init(&s, 0);
    Pthread_create(&p, NULL, child, NULL);
    Sem_wait(&s);
    printf("parent: end\n");
    return 0;
}
```

### Questão 2
O código é:
```c
sem_t s1, s2;

void *child_1(void *arg) {
    printf("child 1: before\n");
    // what goes here?
    Sem_post(&s1);
    Sem_wait(&s2);
    printf("child 1: after\n");
    return NULL;
}

void *child_2(void *arg) {
    printf("child 2: before\n");
    // what goes here?
    Sem_post(&s2);
    Sem_wait(&s1);
    printf("child 2: after\n");
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t p1, p2;
    printf("parent: begin\n");
    // init semaphores here
    Sem_init(&s1, 0);
    Sem_init(&s2, 0);
    Pthread_create(&p1, NULL, child_1, NULL);
    Pthread_create(&p2, NULL, child_2, NULL);
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("parent: end\n");
    return 0;
}
```

### Questão 3
O código é:
```c
typedef struct __barrier_t {
    // add semaphores and other information here
    sem_t sem1, sem2;
    int num_arrived;
    int num_threads;
} barrier_t;


// the single barrier we are using for this program
barrier_t b;

void barrier_init(barrier_t *b, int num_threads) {
    // initialization code goes here
    Sem_init(&b->sem1, 1);
    Sem_init(&b->sem2, 0);
    b->num_arrived = 0;
    b->num_threads = num_threads;
}

void barrier(barrier_t *b) {
    // barrier code goes here
    Sem_wait(&b->sem1);
    b->num_arrived++;
    if (b->num_arrived == b->num_threads){
        Sem_wait(&b->sem2);
    }
    Sem_post(&b->sem1);
    Sem_wait(&b->sem2);
    Sem_post(&b->sem2);
}
```

### Questão 4
O código é:
```c
typedef struct __rwlock_t {
    sem_t lock;       
    sem_t writelock;  
    int num_readers;  
} rwlock_t;


void rwlock_init(rwlock_t *rw) {
    Sem_init(&rw->lock, 1);
    Sem_init(&rw->writelock, 1);
    rw->num_readers = 0;
}

void rwlock_acquire_readlock(rwlock_t *rw) {
    Sem_wait(&rw->lock);
    rw->num_readers++;
    if (rw->num_readers == 1){
        Sem_wait(&rw->writelock);
    }
    Sem_post(&rw->lock);
}

void rwlock_release_readlock(rwlock_t *rw) {
    Sem_wait(&rw->lock);
    rw->num_readers--;
    if (rw->num_readers == 1){
        Sem_post(&rw->writelock);
    }
    Sem_post(&rw->lock);
}

void rwlock_acquire_writelock(rwlock_t *rw) {
    Sem_wait(&rw->writelock);

}

void rwlock_release_writelock(rwlock_t *rw) {
    Sem_post(&rw->writelock);

}
```