#!/usr/bin/python

import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

while True:
	strGPRMC=mc.get("GPRMC")
	strGPGGA=mc.get("GPGGA")
	strGPVTG=mc.get("GPVTG")

	print strGPRMC
	print strGPGGA
	print strGPVTG
			


