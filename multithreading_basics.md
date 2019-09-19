## what is the difference between process and thread?
Processes have clean model for sharing state information between parent and child:
file tables are shared and user address spaces are not. It's impossible for one process
to accidentally overwrite the virtaul memory of another. But to share information,
they have to explicitly use IPC mechanisms.
Thread is a logical flow that runs in the context of a process.
Each thread has its own thread context:
incliding TID, stack, stack pointer, program counterm general-purpose registers,
and condition codes. All threads running in process share the entire virtual address space of that process (including its code, data, heap, shared libraries, and open files).
AThread context switch is faster than a process cntext switch. 
Another difference is that threads are not organized in a parent-chil hierarchy.
The threads associated with a process form a pool of peers, independent of which
threads were created by which other threads.
A thread can kill any of its peers. 

## what is a shared resource?
it's a resource (e.g. address space, file descriptors, ..) that is shared (between processes, threads)

## whta is a race?
when two orr more threads can access shared data and they try to change it at the same time.
thread scheduling can swap betwwen threads any time, and you don't know the order in which the threads will attempt to access the shared data.

## how to protect shared resource?
it's called syncronization of threads, and usually it's done with a semaphore

## what is a mutex? and how to use them in Python?
Mutex is a binary semaphore, used to provide mutual exclusion, so that each thread had mutually exclusive access tothe shared variable while it's executing the instructions in its critical section. 

## why do we use context managers for mutexes?

## what is a semaphore?
a global variable, with a nonnegative integer value that can only be manipulated by two special operations
- P - if s is nonzero, it decrements s and returns immediately. If s is zero, then suspend the thread until s becomes non zero and the thread is restarted by V
operation. After restarting, the P decrements s and returns control to the caller
- V - increments s by 1. If there are any tthreads blocked at P, waiting for s to become nonzero,
the V restarts exactly one of themm which then completes its P operation by decrementing s.
Performin P operation on a mutex is called locking the mutex.
Performing the V operation is called unlocking the mutex.

## what is a condition variable?
a variable that is used for scheduling accesses to shared resources.
it can be used to wait for some event to happen and then get exclusive access to a shared resource
it's possible to have multiple condition variables share one lock, which allows
coordinating exclusive access to a shared resource
between different tasks interested in particular states of that shared resource

## what is GIL in Python?
GIL is a single lock on the interpreter which adds a rule that execution of any Python bytecode requires acquiring the interpreter lock. This prevents deadlocks,
but effectivelt makes any CPU-bound Python program single-threaded.

