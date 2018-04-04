#!/usr/bin/python

import memcache
from time import sleep

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# read the GPS sentences once per second from the local memcached service
while True:
	strGPRMC=mc.get("GPRMC")
	strGPGGA=mc.get("GPGGA")
	strGPVTG=mc.get("GPVTG")

	print strGPRMC
	print strGPGGA
	print strGPVTG
			
	sleep(1)

