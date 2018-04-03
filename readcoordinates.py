#!/usr/bin/python

import memcache
import serial

serial0=serial.Serial(port='/dev/serial0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
print("Connected to " + serial0.portstr)

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# we'll want to set the GPRMC key to the device's current position
mc.set("GPRMC", "Recommended Minimum Coordinates")
mc.set("GPGGA", "Essential Fix Information")

# we'll read line as an array of characters from the serial port
aryLine=[]

while True:
	for char in serial0.read():
		aryLine.append(char)
		if char=='\n':
			lstNMEASentence=[]
			strSentence=""

			# form strSentence, a comma-separated sentence from the serial output
			length=len(aryLine)
			for character in aryLine:
				strSentence=aryLine+character

			# print the sentence if the data type is GPRMC (Recommended Min Coordinates)
			lstNMEASentence=strSentence.split(",")

			# the first field of the NMEA Sentence is the data type
			strGPSDataType=lstNMEASentence[0]

			# store the sentence in memcached if we have a GPRMC sentence
			if strGPSDataType=='$GPRMC':
				mc.set("GPRMC", strSentence)

			aryLine=[]
			print mc.get("GPRMC")
			break

serial0.close
