 > Vidath Dissanayake | Sri Lanka
> Links: [Computer Networking](Computer%20Networking.md)

# Modulation Techniques

![Modulation](assets/images/Modulation.svg)

Carrier waves should be used to transmit data between two locations. A carrier wave is a wave that flows through a transmission media and which is used to carry data.

Data that is available as an electronic wave should be entered into the transmission media. For that, the data available in the source of data should be connected to carrier waves. When doing so, the carrier wave or the high frequency wave should be created by changing the frequency, amplitude, and phase of the wave. This process is called modulation.

The process of modulation is divided into two portions as digital and analog due to the reason of availability of digital as well as analog data on certain occasions. 


# Analog Data Modulation

## Amplitude Modulation (AM)

Changing the height of the wave on each occasion to suit the transmitted electronic wave (data) is called amplitude modulation.

![Amplitude Modulation](assets/images/AM.png)

<u>Advantages:</u>
- It is very easy to modulate and demodulate.
- Low cost.

<u>Disadvantages:</u>
- May be affected by external noise during transmission.

## Frequency Modulation (FM)

The carrier wave that is created by increasing the amount of waves at locations where the voltage of the transmittable wave available in the source of data device is high and decreasing the number of wave frequency at the locations where the voltage is low is called frequency modulation.

![Frequency Modulation](assets/images/FM.png)

## Phase Modulation (PM)

Creating the carrier wave by converting the wave into an angle of 180$\degree$ where the voltage of the transmitted wave is high, and creating the angle of the wave as 0$\degree$ at locations where the voltage is low is called phase modulation.

![Phase Modulation](assets/images/PM.png)


# Digital Data Modulation

The way of forwarding digital data into transmission media is called digital data transmission or digital data modulation.

There are 3 types of digital data modulation. These 3 ways are similar to analog data transmission.
1. Amplitude Shift Keying (ASK)
2. Frequency Shift Keying (FSK)
3. Phase Shift Keying (PSK)

## Amplitude Shift Keying (ASK)

The shape of the digital wave forwarded to the transmission media is created within amplitude shift keying by decreasing the height of the carrier wave in places relevant to 0 bits and increasing the height of the wave in places relevant to 1.

![Amplitude Shift Keying](assets/images/ASK.png)

## Frequency Shift Keying (FSK)

The shape of the digital wave forwarded to the transmission media is created under frequency shift keying by increasing the number of waves in places relevant to '1' bits and decreasing the amount of wave in places relevant to '0' bits.

![Frequency Shift Keying](assets/images/FSK.png)

## Phase Shift Keying (PSK)

Conversion of the carrier wave into an angle of 180$\degree$ in places relevant to '1' bit and converting the same as 0$\degree$ in places relevant to 0 when forwarding data into transmission media is done in PSK.

![Phase Shift Keying](assets/images/PSK.png)


# Multiplexing

Multiplexing combines multiple analog or digital signals bound for transmission through a single transmission line. That means, using a common transmission medium, to transmit more than 1 signal simultaneously is called as multiplexing. 

In this process, a special device is used to forward the data received through several transmission media into a single transmission media, called a multiplexer (Mux).

Suppose that 2 devices connected to a transmission media have been named device 1 and device 2 and 2 individuals are surfing the internet through those devices. The data transmitted through the computers they use are received by the multiplexer.

When the data transmitted from the two devices are received by the receiving end, they are forwarded to the de-multiplexer (DMux). Then, by that device, the data signals received from device 1 ad device 2 are separated into 2, and they are forwarded to the receiving devices.

![Multiplexing](assets/images/Multiplexing.png)

The cost can be reduced by facilitating the signals of several devices to be flown through a single transmission media.

![[assets/images/Multiplexing.svg]]

## Frequency Division Multiplexing (FDM)

FDM is based on the concept of sharing bandwidth of a common communication channel. FDM allows few users to send their data using single communication medium without broadcasting to the air.

## Wave Division Multiplexing (WDM)

Logical division of the bandwidth of the transmission media into channels and transmit data to each device through those channels is done using wave division multiplexing. 

## Time Division Multiplexing (TDM)

According to TDM, all signals to be transmitted are not transmitted simultaneously, and they transmit one by one. Therefore, each signal will be transmitted within the transmission medium for a very short time period only.

![Time Division Multiplexing](assets/images/TDM.png)