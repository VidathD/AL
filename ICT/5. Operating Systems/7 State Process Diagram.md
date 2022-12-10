 > Vidath Dissanayake | Sri Lanka
> Links: [Operating Systems](Operating%20Systems.md)

# 7 State Process Diagram

![7 State Process Diagram TG](assets/images/7%20State%20Process%20Diagram%20TG.png)

![7 State Process Diagram](assets/images/7%20State%20Process%20Diagram.svg)

## 4. Blocked State

A process turns into this state until the external facts are fulfilled to continue the relevant process further. As soon as those sources are received, the blocked state changes into the running state. Main instances that turn into this condition are, input and output units. 

For example, when a large number of typed pages are set to be printed, relevant data are directed to the printer and continuous printing. Then, if the number of papers are finished, the process turns into blocked and waiting state. When the printer is again prepared, it turns into ready and waiting state.


## 5. Terminated State

Ending a process or stopping completely is called terminated state. The process that turns into this state is removed from the main memory.

Reasons affecting terminating of a process.
1. Ending the time of the process.
2. Non-availability of the required resources of the process.
3. Runtime errors.
4. Stopping due to the need of the operating system.


## 6. Swapped Out and Waiting State

Processes that were initially in ready state but were swapped out of main memory and placed into virtual memory by scheduler are said to be in swapped out and waiting state.

The process will transit back to ready state whenever the process is again brought into the main memory.


## 7. Swapped Out and Ready State

If a process becomes blocked while in operation, that process will be removed from the processor and forwarded into virtual memory. This is called, swapped out ready state.

The reasons for the process to become suspended are the interrupts from the CPU.
