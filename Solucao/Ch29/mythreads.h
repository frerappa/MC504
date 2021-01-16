#ifndef __MYTHREADS_h__
#define __MYTHREADS_h__

#include <pthread.h>
#include <assert.h>
#include <sched.h>

void Pthread_create(pthread_d *thread, const pthread_attr_t *attr, void *(*start_routine)(void*), void *arg){
    int rc = pthread_create(thread, attr, start_routine, arg);
    assert(rc == 0);
}

void Pthread_join(pthread_t thread, void **value_ptr){
    int rc = pthread_join(thread, value_ptr);
    assert(rc == 0);
}
#endif