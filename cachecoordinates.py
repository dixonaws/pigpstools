#!/usr/bin/python

import memcache
import serial

serial0=serial.Serial(port='/dev/serial0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
print("Connected to " + serial0.portstr)

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# we'll want to set the GPRMC key to the device's current position; right now we only care about these two keys
# reference the NMEA sentence structure at http://www.gpsinformation.org/dale/nmea.htm#GGA
mc.set("GPRMC", "Recommended Minimum Coordinates")
mc.set("GPGGA", "Essential Fix Information")

sentence=[]

while True:
	for char in serial0.read():
		sentence.append(char)
		if char=='\n':
			lstNMEASentence=[]
			strSentence=""
			length=len(sentence)
			for character in sentence:
				strSentence=strSentence+character

			# print the sentence if the data type is GPRMC (Recommended Min Coordinates)
			lstNMEASentence=strSentence.split(",")

			# the first field of the NMEA Sentence is the data type
			strGPSDataType=lstNMEASentence[0]

			# store the sentence in memcached with a key that matches the data type
			if strGPSDataType=='$GPRMC':
				mc.set("GPRMC", strSentence) # recommended minimum data for gps
			elif strGPSDataType=='$GPGGA':
				mc.set("GPGGA", strSentence) # fix information
			elif strGPSDataType=='$GPGSA':
				mc.set("GPGSA", strSentence) # overall satellite data
			elif strGPSDataType=='$GPVTG': 
				mc.set("GPVTG", strSentence) # vector track and speed over the ground

			sentence=[]
			
			break

serial0.close

