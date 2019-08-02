#!/usr/bin/env python
import getopt
import socket
import sys
import time

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri


#client = None

def main(limit):  # pragma: no cover
	global client
	num = 0
	while num < 10:
	    path = "coap://192.168.1.108:5683/basic/"
	    counter = ["%s" % num]
	    payload = counter[0]

	    host, port, path = parse_uri(path)
	    try:
	        tmp = socket.gethostbyname(host)
	        host = tmp
	    except socket.gaierror:
	        pass
	    client = HelperClient(server=(host, port))
	    response = client.put(path, payload)
	    print((response.pretty_print()))
	    client.stop()
	    print("num   ===", num)
	    num = num + 1 
	    print("num  2 ===", num)
	    time.sleep(2)

if __name__ == '__main__':  # pragma: no cover
    main(10)

