#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:21:26 2024

@author: mahsa
"""

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            protocol = "TCP"
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            protocol = "UDP"
        else:
            sport = dport = None
            protocol = "Other"

        print(f"Protocol: {protocol}")
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        if sport and dport:
            print(f"Source Port: {sport}")
            print(f"Destination Port: {dport}")
        print("="*50)

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
