virtual memory - a memory access scheme. When using virtual memore, the kernel does not access the memory by its physical location in the hardware. 
Instead, the kernel sets up every process to act as if it had an entire machine to itself.

Memory management unit (MMU) - translates the memory location from the process into an actual physical memory location on the machine, using
a memory address map. The kernel must initialize and maintain this memory address map.

Kernel manages tasks in 4 different areas:
- processes - determines which processes are allowed to use CPU
- memory - keep track of memory - what is currently allocated to a particular process, what is shared and what is free
- device drivers - kernel acts as an interface between hardware and processes
- system calls - processes normally use system calls to communicate with kernel

## what is kernel space and user space?
 
User space - the main memory that the kernel allocates for user processes.

## what is init?

init is a first user-space process which is started by kernel. Its main purpose is to start and stop the essential service
processes on the system

## what is PID1?
process ID of init

## what init systems you know?
System V init
systemd
Upstart

## what is a file descriptor?
file descriptor is an integer number that uniquely identifies an open file in the OS. 
When a process makes a successful request to open a file,
the kernel returns a file descriptor which points to an entry in global file table.
The file table entry contains information as inode if the file,
byte offset and access restrictions.

## what is a socket?
Sockets are the interface that processes use to access to the network through kernel, they represent 
boundary between user space and kernel space. They are often also used for IPC
Socket can be thought as an endpoint for a two-way communication channel. 
Each socket within the network has a unique name associated with it called a socket descriptor - 
an integer that designates socket and allows application programs to refer to it. 

## what is sync syscall? why does anybody use it?
kernel keeps data in memory to avoid doing slow disk reads and writes.
This improves performance, but if the computer crashes, data may be lost or fs could be corrupt,
so this sys call ensures that everything in memory is written to disk.

## how to interact between kernel and user space
system call, ioctl, proc filesystem, netlink socket, ...

## what is netlink in linux?
netlink socket is a IPC for transferring information between user space and kernel space.
Netlink socket uses address family AF_NETLINK 
