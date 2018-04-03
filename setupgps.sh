#!/bin/bash

stty -F /dev/serial0 raw 9600 cs8 clocal -cstopb

#gpsd /dev/serial0 -F /var/run/gpsd.sock

cat /dev/serial0
