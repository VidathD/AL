 > Vidath Dissanayake | Sri Lanka
> Links: [Operating Systems](Operating%20Systems.md)

# Process Transition

The operating system's role is to manage existing and newly created processes by moving them between the 2 states until they finish. For simplicity, modern operating systems supports the idle process, which is always ready to run and never terminates. Newly created processes are created and marked as ready and are queued to run as the single running process terminates, or it is interrupted, it is marked as ready by the OS and the next ready process is continued. Here the OS has the role of dispatcher.

# Process Control Block (PCB)

Process control block (PCB) is a data structure maintained by the OS for every process. The process is identified by an integer process ID (PID). PCB keeps all the information needed to keep track of a process.

| No  | Information            | Description                                                                            |
|:---:|:---------------------- |:-------------------------------------------------------------------------------------- |
|  1  | Process State          | Ready, Running, Waiting, etc…                                                          |
|  2  | Process ID             | Unique identification for each of the processes in the OS.                             |
|  3  | Program Counter        | It is a pointer to the next instruction to be executed for this process.               |
|  4  | CPU Registers          | Various CPU registers where process need to be stored for execution for running state. |
|  5  | Memory Management      | This includes the information of page table, memory limits segment table.              |
|  6  | I/O Status Information | This includes a list of I/O devices allocated to the process.                                                                                       |

Simplified Diagram of PCB:
![Simplified Diagram of PCB](assets/images/Simplified%20Diagram%20of%20PCB.svg)

# Context Switching

A contest switch is the mechanism to store and restore the state or context of a CPU, in a process control block, so that the process execution can be resumed from the same point at a later time.

Using this technique, a context switcher enables multiple processes to share a single CPU. Context switching is an essential part of a multitasking OS features.

When the scheduler switches the CPU from executing one process to another, the context switcher saves the content of all processor registers for the processing being removed from the CPU in its PCB.

Context switch time is pure overhead. Context switching can significantly affect performance, as modern computers have a lot of general and status registers to be saved.