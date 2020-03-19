# TCP/IP Model

###### Application -> Transport -> Network -> Data Link -> Physical

###### Application
* Writing/ Reading data off to the network
* Application levell protocol
    * www
    * SMTP
    * voip
    * DNS -> ROOT DNS => Top Level domain (.com, .edu) => authoritative servers
* type -> Client-Server, P2P


###### Transport
* the transport layer takes messages from the network to applications
* TCP, UDP
    * TCP -> reliable
        * ssh, http, https, ftp
        * Full Duplex
        * header -> source, destination, sequence number, ack number, checksum
        * header flags => ACK, RST, SYN, FIN, PSH, URG
        * connection oriented
            * three way handshake
                * -> SYN <- SYN + ACK -> SYN + ACK
            * release -> FIN
        * RTT (Round Trip Time) of a connection is the amount of time it takes to send a packet and receive its acknowledgment
    * UDP -> May or may not get delivered, may get delivered out of order or changed or missing or corrupted data
        * header -> source , destination, length, checksum
        * data
        * uses streaming, dns
        * customizable
* Multiplexing -> multiplexing allows messages to be sent to more than one destination host via a single medium
* Demultiplexing -> Demultiplexing knows which application to forward the recieved message
* sockets are gateways between applications and the network -> associated IP and a port number (0 - 65,535)