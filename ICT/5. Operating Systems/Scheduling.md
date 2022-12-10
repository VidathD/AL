 > Vidath Dissanayake | Sri Lanka
> Links: [Operating Systems](Operating%20Systems.md)

# Types of Scheduling

## Long-Term Scheduling (Job Scheduling)

It determines which programs are admitted to the system for processing. This long-term scheduler selects processes ad loads them into memory for execution.

## Mid-Term Scheduling

This is in charge of swapping processes between the main memory and the secondary storage (Suspend and resume).

## Short-Term Scheduling (Low Level Scheduling)

Determines which ready process will be assigned the CPU when it next becomes available. This is also called dispatcher. Very frequently doing its job.

# Scheduling Policies

## Non-Pre-emptive

- Once a process is in the running state, it will continue until it terminates or blocks itself for I/O. 

## Pre-emptive

- Currently, a running process may be interrupted and moved to the ready state by OS. 
- Allows for better service, since any one process cannot monopolize the processor for a very long time.
- If a process is running in the CPU, then that process can be forcefully removed from the CPU and allocated to another process. This is called pre-emptive.

# Scheduling Algorithms

## First Come, First Served (FCFS)

| Process | AT  | BT  | CT  | TT (CT-AT) | WT (TT-BT) | RT  |
|:-------:| --- | --- | --- | ---------- | ---------- | --- |
|   P1    | 2   | 2   | 4   | 2          | 0          | 0   |
|   P2    | 0   | 1   | 1   | 1          | 0          | 0   |
|   P3    | 2   | 3   | 7   | 5          | 2          | 2   |
|   P4    | 3   | 5   | 12  | 9          | 4          | 4   |
|   P5    | 4   | 4   | 16  | 12         | 8          | 8   |

- AT – Arrival Time.
- BT – Burst Time.
    - Processor time required to complete the process or the time during which the process is running.
- CT – Completion Time.
    - Time when the process has been completed
- TT – Turnaround Time.
    - Time taken for a particular process to complete from submission time to completion
    - CT-AT
    - WT+BT
- WT – Wait Time
    - How much time the process spends in the ready queue waiting its turn to get on the CPU.
    - TT-BT
- RT – Response Time.
    - Time taken in an interactive program from the issuance of a command to commence a response to that command.
    - First time the process comes and at what time that process has been allocated to the CPU.


Gantt Chart: 
![Gantt Chart 1](assets/images/Gantt%20Chart%201.svg)


**Q1:**

| Process | AT  | BT  | CT  | TT (CT-AT) | WT (TT-BT) | RT  |
|:-------:| --- | --- | --- | ---------- | ---------- | --- |
|   P1    | 2   | 1   | 12  | 10         | 9          | 9   |
|   P2    | 1   | 5   | 11  | 10         | 5          | 5   |
|   P3    | 4   | 1   | 16  | 12         | 11         | 11  |
|   P4    | 0   | 6   | 6   | 6          | 0          | 0   |
|   P5    | 2   | 3   | 15  | 13         | 10         | 10  |
![Gantt Chart 2](assets/images/Gantt%20Chart%202.svg)

## Other Algorithms

Further, we have to discuss shortest job first scheduling, round-robin scheduling and priority based scheduling.