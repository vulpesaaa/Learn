import scapy
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether

from readexcel import extract

file = r'C:\Users\Administrator\Desktop\抓包\端口值.xlsx'
excel_list = extract(file)

key = []
for p in excel_list:
    key.append(p[0])
print(key)

value = []
for p in excel_list:
    value.append(int(p[1]))
print(value)



srcmac = "00:1B:44:11:3A:B7"
dstmac = "b8:81:98:1b:15:57"
dstip = "192.168.1.10"


pkt = (Ether(src=srcmac, dst=dstmac)/
       IP(dst=dstip)/
       TCP(sport=value)
       )

# 发送2层
sendp(pkt, inter=0.2, iface="WLAN", count=1)