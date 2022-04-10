#For the Nixu 2018 challenge Phishcap - part 3

from scapy.all import *

#open the file in question
pcap_file = rdpcap('challenge.pcap')
#take only ICMP packets from all packets
icmp_packets = [p for p in pcap_file if ICMP in p]
#parse the packets from infected machine to the attacker
target_packets = [p for p in icmp_packets if p[IP].src == 'x.x.x.x' and p[IP].dst == 'x.x.x.x']

#take all the payloads in the ICMP packets and parse them in to a array
#the payload is a file with binary content cut in to parts
data = []
for t in target_packets:
    l = t.getlayer(Raw).load
    data.append(l)
#join the binary as one
to_disk = b''.join(data)
#write the binary to a file
with open('exfiltered_data.pdf','wb') as f:
    f.write(to_disk)

