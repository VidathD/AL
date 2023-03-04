> Vidath Dissanayake | Sri Lanka
> Links: [Computer Networking](Computer%20Networking.md)

How multiple networks are interconnected to form the internet.

# A Device to Connect Two or More Networks

## Gateway

A network gateway joins 2 networks, so the devices on 1 network can communicate with devices on another network. Without gateways, you won't be able to access the internet, communicate and send data back and forth within a network.

## Default Gateway

A default gateway lets devices in one network to communicate with devices in another network.

When the IP address available in the data packet being transmitted cannot be found in the internal network, on such occasions that data is being transmitted by a device available in a TCP/IP network to another device available in the same network. 

The gateway established to forward the data packet is called the default gateway.

External device.


## IP Addressing

IP Stands for Internet Protocol. An IP address is a unique identifier given to every machine or device in a network.

An IP address served 2 primary functions. It is used as an interface identification for a network of machines, and it also serves to provide a location of that machine.
   > Every person has an address to inform the location where he is residing. Others send letters to him using his address. In the same manner, an address should be used to send messages from one computer to another in a network. It is named as IP addresses. 
   > In a network, computers as well as other devices, routers, printers, switches, etc… are also identified using IP addresses.

## Internet Assigned Number Authority (IANA)

The institution which functions with regard to internet protocols is called IANA.

IANA is an internet specific organization that gives out IP addresses in a systematic, organized and consistent manner that benefits everyone. 

IANA introduced 2 IP versions as,
1. IPv4
2. IPv6

# IPv4

This protocol was 1st introduced to the world on the 1st of January 1983. The address prepared using this version consist of 32 bits that has been portioned to 8 bits (octets).

**E.g:**
> 192.168.102.242
> Each portion allow from 0 to 255 number range.

Can be written in binary values too. But when ordinary people work with numbers, binary values are not used. 

> 192.168.102.242
> 1100000.10101000.01100110.11110010

## How to Identify a Valid IPv4

An IPv4 should consist of 4 octets. One part may be spread between a range of 0 to 255 decimal numbers.

## Loopback Number

An address sends outgoing signals back to the same computer is identified as a loopback number. The loopback IP number is **127.0.0.1**. It is used for testing purposes. 

For example, suppose that a web developer who develops a dynamic website wants to store and retrieve data. At the time of developing this website, it is difficult for him to upload web pages into a web server and continue the creation of the website. Therefore, the computer can be used as a server until uploading the website and the relevant data to a server. For that, special software has to be installed to make the computer a server and enter the data and the web pages and develop the website.

## IP Address Classes

IP addresses used in computer networks are classified into several classes according to international accords. According to this classification, there are 5 main classes classified depending on the size of them as follows.

### Class A

- Used for the networks with a large number of hosts. 
- The 1st bit of an octet of an address of this class starts with 0. 
- Can connect more than 16 million hosts (16777214). 
- Class A networks are from 1.0.0.0 to 126.0.0.0.

### Class B

- Used for networks with a medium number of hosts.
- 1st 2 bits of the 1st octet starts with 10. 
- Class B networks are from 128.0.0.0 to 191.255.0.0.
- Can connect 65534 hosts.

### Class C

- Used for small scale host networks.
- 1st 3 bits of the 1st octet starts with 110.
- Class C networks starts from 192.0.0.0 to 233.0.0.0
- Can connect 254 hosts.

### Class D

- Reserved for multicast groups.

### Class E 

- Reserved for future use or research and development purpose.


## Subnet Mask

### Class A

Formula: `Net.Host.Host.Host`
Binary: `11111111.00000000.00000000.00000000`
Decimal: `255.0.0.0`

### Class B

Formula: `Net.Net.Host.Host`
Binary: `11111111.11111111.00000000.00000000`
Decimal: `255.255.0.0`

### Class C

Formula: `Net.Net.Net.Host`
Binary: `11111111.11111111.11111111.00000000`
Decimal: `255.255.255.0`

When an IP address is included in a computer, the subnet mask is also entered. Therefore, when an IP address is indicated, the subnet mask is also indicated as follows.

**E.g:**
> IP: `192.168.1.50`
> Default subnet mask: `255.255.255.0`

- The subnet mask is important to identify the number of computers that can be entered into the network.
- The subnet mask has been created with the maximum bit values that can be entered into an address of the network.

## Subnetting

Division of a computer network into small networks is called subnetting.

Subnetting is a technique used to overcome the problem of depletion of network address of the 32 bit addressing scheme. In subnetting, each physical network is assigned a 32-bit address mask, which is used to identify networks among other networks. All machines in the subnet should have the same subnet mask. 

### Classes Inter-Domain Routing (CIDR)

Instead of full class A, B or C networks, organizations can be allocated any number of addresses using this scheme. This scheme can help reduce the growth of the routing tables. 

| Network Class | Subnet Mask by Decimal Numbers | Subnet Mask by Binary Values        | No. of Changeable Bits for Creating Subnets |
|:-------------:| ------------------------------ | ----------------------------------- |:-------------------------------------------:|
|       A       | 255.0.0.0                      | 11111111.00000000.00000000.00000000 |                     24                      |
|       B       | 255.255.0.0                    | 11111111.11111111.00000000.00000000 |                     16                      |
|       C       | 255.255.255.0                  | 11111111.11111111.11111111.00000000 |                      8                      |


## Private IPs

Three sets of address ranges are used for private use.

### Class A

> Range: `10.0.0.0 - 10.255.255.255`
> CIDR notation: `10.0.0.0/8`

### Class B

> Range: `172.16.0.0 - 172.31.255.255`
> CIDR notation: `172.16.0.0/12`

### Class C

> Range: `192.168.0.0 - 192.168.255.2551
> CIDR notation: `192.168.0.0/16`

## Dynamic Host Configuration Protocol (DHCP) Server

DHCP is a protocol used to assign IP addresses to arriving hosts rather than a network administrator manually assigning an IP address to each arriving host, the DHCP will assign IP addresses automatically.

## Finding the Path to the Destination

When data leaves the sources towards the destination, it needs to be routed through a series of networking devices to reach the destination. Routers take care of the job of routing the data from the sources to the destination. <u>Routing is the process of finding an efficient path from a source to a given destination through the network.</u>

Routers are special networking devices that are capable of communicating with similar devices over the network, collaborate among themselves and find paths to arriving data.  Routers maintain a table of reachable destinations through them, and these tables are called routing tables. Routers exchange these routing tables with other routers in the network from time to time to update the route details.

### Packet Switching

When a message is generated at the source, it is broken down into smaller chunks called packets. Each packet is assigned unique information to identify itself, switching information is added in the header of each packet and is transmitted independent of other packets.