### Pi GPS Tools

These programs query /dev/socket0 for GPS information, and write the resulting sentences to a local memcached service. A simple program is also provided to query the memcache service and print it to stdout once per second. When cashcoordinates is runing, the local memcached service always contains the current location of the device.

