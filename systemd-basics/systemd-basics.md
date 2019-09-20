## Who are UNIX daemons?
a long-running background process, owned by the init process and not connected to a controlling Terminal


## why systemd?
systemd provides
- parallel starto of system services at boot time
- on-demand activation of daemons
- dependency-based service control-logic
systemd is a system and service manager for Linux OS

## what problems did it solve?
- optimizing boot times
- keeping track of processes - using control groups - they allow the creation of hierarchy of groups of processes
- parallelizing socket/bus services - start all daemons in parallelm without any further synchronization,
start services when they are first accessed (lazy-loading)
- parallelize file system jobs - using autofs system - set up an autofs mount point, and replace it by the real mount
when our fs finished fsck and quota due to normal boot-up
- get rid of shell scripts in the boot process (keeping the first user PID small)

## Who wrote it?
Lennart Poettering (Red Hat)
Kay Sievers (Novell)
and many more

## What is a service?
daemon that can be started, stopped, restarted, reloaded

## What is a target?
unit type that is used for logical grouping of services, it references other units, which 
can be controlled together

## What is a systemd-analyze?
tool for analyzing and debugging system manager
determine system boot-up performance statistics and retrieve otherr state and tracing information
fron the system and service manager, and to verify the correctness of unit files.
