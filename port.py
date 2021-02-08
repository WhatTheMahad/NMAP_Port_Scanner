#!/bin/bash/python3
import nmap

scanner = nmap.PortScanner()
print ("NMAP Port_Scanner.\n By @WhatTheMahad")
ip_address = input ("Enter IP: ")
print ("IP is: ", ip_address)
type(ip_address)
resp = input ("""\n Enter Fucntion to Perform
				1. SYN ACK Scan
				2. UDP Scan
				3. Comprehensive Scan \n""")
print("You selected option ", resp)


if resp == '1':
	print("NMAP Version: ", scanner.nmap_version())
	scanner.scan(ip_address,'1-1024','-v -sS')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_address].state())
	print(scanner[ip_address].all_protocols())
	print("Open Ports: " ,scanner[ip_address]['tcp'].keys())

elif resp == '2':
	print ("NMAP Version: ",scanner.nmap_version())
	scanner.scan(ip_address,'1-1024','-v -sU')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_address].state())
	print(scanner[ip_address].all_protocols())
	print("Open Ports: " ,scanner[ip_address]['udp'].keys())

elif resp == '3':
	print ("NMAP Version: ",scanner.nmap_version())
	scanner.scan(ip_address,'1-1024','-v -sS -sV -sC -A -O')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_address].state())
	print(scanner[ip_address].all_protocols())
	print("Open Ports: " ,scanner[ip_address]['tcp'].keys())



elif resp >= 20:
	print("Invalid")