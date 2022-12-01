import scapy
from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether

"""
sr1()：返回三层数据包的应答数据包
srp():返回二层数据包的应答数据包
"""

sr1(IP()/)