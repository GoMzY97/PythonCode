import socket
import termcolor

def scan(target, posrts):
	print('\n ')
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened"+ str(port))
		sock.closed()
	except:
		pass
		#print("[-] Port Closed"+ str(port))

targets = input("[*] ENter targets to scan(split them by ,): ")
ports =int(input("[*] Enter How many ports you want to scan: "))
if ',' in targets:
	print("[*] Scanning Multiple Targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
