> Vidath Dissanayake | Sri Lanka
> Links: [Computer Networking](Computer%20Networking.md)

When creating a computer network, the ways of connecting computers to that network both physically and logically is called network topology. There are several network topologies.
1. Bus topology
2. Star topology


# Bus Topology

- A bus topology is installed, connecting computers using a main wire and a drop line cable. The cable used from the main cable to the device connected to the computer is called drop line cable.
- Taps are used to connect the drop line cable to the main cable.
- Two cable terminators are connected to the both ends of the main cable.
- When one computer sends a signal up to the main cable, all computers connected with the network receive the data, but based on the address, the receiver obtains the data and other computers reject the data.

- The speed of the bus topology is lower than other network topologies. The reason is, only one computer can transmit data at a given time.
- A coaxial cable is used as the main cable.

<u>Advantages</u>:
- The length of the wires is less than that of star topology.
- As the computers are connected in a linear method, the construction is easy. 
- Expenditure is less when compared to other topologies.

<u>Disadvantages</u>:
- If the main cable becomes deactivated, the whole network becomes deactivated. 
- Difficult to troubleshoot.
- Two special devices have to be fixed to the terminals of the main cables.
- Though transmitted data in not required for other computers, the data forwarded to a selected computer in the network is transmitted to all the computers in the network. 

![Bus topology](assets/images/Bus%20topology.png)


# Star Topology

- A network that is established connecting all the computers to a single device (switch/hub) is called star topology.
- Nowadays, hubs are rarely used. Instead, switches that have the ability to carry data efficiently.
- This topology is used to establish LAN in schools, offices, and other institutions.

<u>Advantages</u>:
- Easy to troubleshoot.
- Fixing and removing computers can be done easily.

<u>Disadvantages</u>:
- More wires are required than linear structure.
- If the hub or switch becomes deactivated, all the computers in the network, all the computers in the network becomes deactivated.
- As the central unit is expensive, 

![Star Topology](assets/images/Star%20Topology.png)


# Ring Topology

- Ring networks are created with wires made like a ring. 
- Data of this network which doesn't use a central device flow to a single direction only.
- Data transmitted within a network flows from one computer to another. A computer is connected with 2 other computers via cables.

<u>Advantages</u>:
- As the data is flown to a single direction, data transmission is fast.
- In this network, data is transmitted according to the method of token ring, which is a special data transmission methodology. Therefore, no data collisions.
- No hub or switch required.

<u>Disadvantages</u>:
- If an error occurs in the main cable, it causes the network to be collapsed.
- Expansion is difficult.

![Ring Topology](assets/images/Ring%20topology.png)


# Simple Topology/Point to Point Connection

Connecting 2 devices on a network using a single cable is called simple topology.

For example, connecting a computer with another computer, a switch, a router, or a hub can be mentioned.

![Point to point](assets/images/Point%20to%20point.png)