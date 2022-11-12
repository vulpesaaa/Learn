import scapy
from scapy.all import *
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether

srcmac = "00:1B:44:11:3A:B7"
dstmac = "b8:81:98:1b:15:57"
dstip = "192.168.1.10/30"
ether = Ether(src=srcmac, dst=dstmac)
ip = IP(dst=dstip) / fuzz(UDP())

udp_fuzzing = ether / ip
# 发送2层
sendp(udp_fuzzing, inter=0.2, iface="WLAN", count=20)
