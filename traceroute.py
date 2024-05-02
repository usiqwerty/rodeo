# Importing Libraries
import socket

from scapy.all import IP, UDP, sr1

from route import Route


def traceroute(destination, max_hops=30, timeout=2, display=True) -> list[str, None]:
    destination_ip = socket.gethostbyname(destination)
    port = 33434
    ttl = 1

    route = []
    while True:
        # Creating the IP and UDP headers
        ip_packet = IP(dst=destination, ttl=ttl)
        udp_packet = UDP(dport=port)

        # Combining the headers
        packet = ip_packet / udp_packet

        # Sending the packet and receive a reply
        reply = sr1(packet, timeout=timeout, verbose=0)

        node = None
        if reply is None:
            if display: print(f"{ttl}\t*")
        elif reply.type == 3:
            # Destination reached, print the details
            node = reply.src
            if display: print(f"{ttl}\t{node}")
            break
        else:
            # Printing the IP address of the intermediate hop
            node = reply.src
            if display: print(f"{ttl}\t{node}")
        route.append(node)

        ttl += 1

        if ttl > max_hops:
            break
    return route
