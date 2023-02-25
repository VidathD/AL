> Vidath Dissanayake | Sri Lanka
> Links: [Computer Networking](Computer%20Networking.md)

Imagine that A and B means two computers available in a network and data from A computer has to be transmitted to B computer. In such an occasion, data available in A computer should be released to the cable by which the two computers are connected.

The way of releasing and the connected technological methodologies are discussed below. A bus network is used for that. 


# Way of Using the Transmission Media According to the Bus Topology

A single wire is used to transmit data in a bus topology, to which the devices of the network are connected. Accordingly, all the devices connected to the transmission media transmit data among other devices using a single transmission media (main cable).

The main possible issue of this is, if 2 devices transmit data at the same time, to the sides opposite to each other, signals relevant to data gets disrupted due to the collision.

The following diagram shows the way of data flowing after forwarding to the transmission media by A and B computers. Accordingly, when data is transferred from several devices to the transmission media, data should be approached to the transmission media in a manner where they do not collide. The methodologies introduced for this are described as follows.

![](assets/images/BUS%20collision.png)


## Pure ALOHA

Forwarding data to the transmission media by the transmitter when the frames that are used to carry signals within transmission media becomes free is called ALOHA protocol.

Creation of these protocols was commenced under the leadership of Norman Abrahamson in Hawaii.


### ALOHA Protocol Steps

1. Inquiring whether the frames are free. 
2. Forwarding signals to the transmission media, if free.
3. Waiting for the acknowledgement signal.
4. If the acknowledgement signal is received, forwarding next data to the frame.
5. If the acknowledgement signal is not received, wait for some time period and resend the frame of data again.

### Weaknesses of ALOHA Protocol

Inability to confirm whether the data is already being transmitted in the transmission medium. Therefore, possibility of damaging the frames is high.

![](assets/images/Pure%20ALOHA.png)


## Slotted ALOHA

![](assets/images/Slotted%20ALOHA.png)

