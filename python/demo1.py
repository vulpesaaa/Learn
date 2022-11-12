from pyx import *
from scapy.all import *
from scapy.layers.inet import IP, ICMP

p = IP()/ICMP()
